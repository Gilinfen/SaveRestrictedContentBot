<h1 align="center">
  <b>保存受限内容的机器人</b>
</h1> 

联系: [Telegram](https://t.me/MaheshChauhan)

这是一个稳定的 Telegram 机器人，用于获取受限消息，并支持自定义缩略图，由 Mahesh Chauhan 制作。

- 支持公共和私人聊天
- 支持私人媒体的自定义缩略图
- 支持文本和网页媒体消息
- 速度更快
- 支持强制关注
- 为了从机器人那里保存消息，请使用以下格式发送链接：`t.me/b/bot_username/message_id`（使用 Plus Messenger 获取 `message_id`）
- `/batch` - （仅限拥有者）使用此命令一次保存多达 100 个文件的私人或公共受限频道的内容。
- `/cancel` - 使用此命令停止批量操作
- 增加了时间延迟以避免 FloodWait 并保证用户账号安全。

# 变量

- `API_ID`
- `API_HASH`
- `SESSION`
- `BOT_TOKEN`
- `AUTH` - 拥有者的用户ID
- `FORCESUB` - 公共频道用户名（不带 '@'）。别忘了将机器人添加为频道管理员。

# 获取 API 和 PYROGRAM 会话字符串的方法：
 
API: [API scrapper Bot](https://t.me/USETGSBOT) 或 [Telegram.org](https://my.telegram.org/auth)

PYROGRAM SESSION: [SessionGen Bot](https://t.me/SessionStringGeneratorRobot) 或者 [![Run on Repl.it](https://replit.com/badge/github/vasusen-code/saverestrictedcontentbot)](https://replit.com/@levinalab/Session-Generator#main.py)

BOT TOKEN: 通过 @Botfather 获取

# 部署

在 `VPS` 上部署

简单方法：

- 安装 docker-compose
- 使用你喜欢的文本编辑器或 nano 编辑 docker-compose.yml 文件中的变量
- 启动容器

```sh
sudo apt install docker-compose -y
nano docker-compose.yml
sudo docker-compose up --build
```

困难方法：

- 在你的 fork 中填写 [此文件](https://github.com/vasusen-code/SaveRestrictedContentBot/blob/master/main/__init__.py) 中的变量，参考 [这张图](https://t.me/MaheshChauhan/36)
- 输入以下所有命令

```sh
sudo apt update
sudo apt install ffmpeg git python3-pip
git clone your_repo_link
cd saverestrictedcontentbot 
pip3 install -r requirements.txt
python3 -m main
```

- 如果你希望机器人在后台运行，请在 `python3 -m main` 之前输入 `screen -S srcb`
- 执行 `python3 -m main` 后，按 `ctrl+A, ctrl+D`
- 如果你想停止机器人，输入 `screen -r srcb`，然后输入 `screen -S srcb -X quit` 以退出屏幕。

在 `Render` 上部署你的机器人

教程 - [点击这里](https://telegra.ph/SRCB-on-Render-05-17)

在 `heroku` 上部署你的机器人

» 方法 - 1:
- Star 这个仓库，然后在桌面模式下 fork 它
- 进入你 fork 的仓库的设置
- 将你的仓库重命名为其他名称
- 点击 [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
 
» 方法 - 2:
- Star 这个仓库，然后在桌面模式下 fork 它
- 在 heroku 中创建应用
- 进入应用的设置 ›› config vars ›› 添加所有变量
- 添加 buildpacks
- 连接到 GitHub 并部署
- 开启 dynos
  
手动部署的 Buildpacks:

- `heroku/python`
- `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`

在 `Okteto` 上部署你的机器人 [无用]

Okteto 教程 - [点击这里](https://telegra.ph/Okteto-Deploy-04-01)

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com)
