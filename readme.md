# ここは何

Contest Notifierというbot (line, discord) のgithubです。詳しくはそれぞれのフォルダーのreadmeを読んでみてください。

# ディレクトリ構成

```
C:.
├─atcoder(ここのGitHubの親ディレクトリ)
│  │  .gitignore
│  │  readme.md
│  │
│  ├─contest-notifier-all
│  │      after_contest.py
│  │      apiAboutmySpreadSheet.md
│  │      example.json
│  │      find_contest.json
│  │      find_contest.py
│  │      get_from_posts.json
│  │      get_from_posts.py
│  │      main.py
│  │      merge.py
│  │      merged.json
│  │      messages.json
│  │      README.md
│  │      sendmessage_discord.py
│  │      sendmessage_google_chat.py
│  │      sendmessage_line.py
│  │
│  └─discord-only
│          apiAboutDiscordDB.md
│          atcoderbot_discord.py
│          colors.ini
│          create_atcoder_role.py
│          kill_atcoderbot_discord.py
│          readme.md
│
├─discord
│      accesstoken.txt
│      channelid.txt
│      dburl.txt
│      to.txt
│
├─google_chat
│      to.txt
│
└─line
        accesstoken.txt
        dburl.txt(送り先を可変にしたいときにGETアクセスで返り値がjson形式でArray[送り先]となるurlを指定してください)
        to.txt(送り先を固定したいときに送り先を改行区切りで入力し利用してください)

```

このようにディレクトリ/ファイルを配置すると正常に動きます。

# 必要モジュール
- Python 3
    必要モジュール：
    - requests
    - beautifulsoup4
    - discord.py