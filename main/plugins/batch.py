#Tg:MaheshChauhan/DroneBots
#Github.com/Vasusen-code

"""
插件为公共和私人渠道!
"""

import time, os, asyncio

from .. import bot as Drone
from .. import userbot, Bot, AUTH
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_bulk_msg
from main.plugins.helpers import get_link, screenshot

from telethon import events, Button, errors
from telethon.tl.types import DocumentAttributeVideo

from pyrogram import Client 
from pyrogram.errors import FloodWait

from ethon.pyfunc import video_metadata
from ethon.telefunc import force_sub

ft = f"要使用这个机器人，你必须加入 @{fs}."

batch = []

@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/cancel'))
async def cancel(event):
    if not event.sender_id in batch:
        return await event.reply("没有批处理活动。")
    batch.clear()
    await event.reply("完成了。")
    
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/batch'))
async def _batch(event):
    if not event.is_private:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft) 
    if s == True:
        await event.reply(r)
        return       
    if event.sender_id in batch:
        return await event.reply("你已经开始了一批，等着它完成吧，你这个傻逼老板!")
    async with Drone.conversation(event.chat_id) as conv: 
        if s != True:
            await conv.send_message("发送给我的消息链接，你想开始保存从，作为对这条消息的回复。", buttons=Button.force_reply())
            try:
                link = await conv.get_reply()
                try:
                    _link = get_link(link.text)
                except Exception:
                    await conv.send_message("没有找到链接。")
                    return conv.cancel()
            except Exception as e:
                print(e)
                await conv.send_message("不能再等你的回复了!")
                return conv.cancel()
            await conv.send_message("发送给我你想从给定的消息中保存的文件/范围的数量，作为对这条消息的回复。", buttons=Button.force_reply())
            try:
                _range = await conv.get_reply()
            except Exception as e:
                print(e)
                await conv.send_message("不能再等你的回复了!")
                return conv.cancel()
            try:
                value = int(_range.text)
                if value > 100:
                    await conv.send_message("单个批处理最多只能获得100个文件。")
                    return conv.cancel()
            except ValueError:
                await conv.send_message("Range必须是整数!")
                return conv.cancel()
            batch.append(event.sender_id)
            await run_batch(userbot, Bot, event.sender_id, _link, value) 
            conv.cancel()
            batch.clear()

async def run_batch(userbot, client, sender, link, _range):
    for i in range(_range):
        timer = 60
        if i < 25:
            timer = 5
        if i < 50 and i > 25:
            timer = 10
        if i < 100 and i > 50:
            timer = 15
        if not 't.me/c/' in link:
            if i < 25:
                timer = 2
            else:
                timer = 3
        try: 
            if not sender in batch:
                await client.send_message(sender, "Batch completed.")
                break
        except Exception as e:
            print(e)
            await client.send_message(sender, "Batch completed.")
            break
        try:
            await get_bulk_msg(userbot, client, sender, link, i) 
        except FloodWait as fw:
            if int(fw.x) > 299:
                await client.send_message(sender, "Cancelling batch since you have floodwait more than 5 minutes.")
                break
            await asyncio.sleep(fw.x + 5)
            await get_bulk_msg(userbot, client, sender, link, i)
        protection = await client.send_message(sender, f"Sleeping for `{timer}` seconds to avoid Floodwaits and Protect account!")
        await asyncio.sleep(timer)
        await protection.delete()
            
