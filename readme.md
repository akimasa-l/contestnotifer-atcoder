# ここは何

Contest Notifierというbot (line, discord) のgithubです。詳しくはそれぞれのフォルダーのreadmeを読んでみてください。

# ディレクトリ構成

```
C:.
├─atcoder(ここのGitHubの親ディレクトリ)
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
        to.txt

```

このようにディレクトリ/ファイルを配置すると正常に動きます。

# 必要モジュール
- Python 3
    必要モジュール：
    - requests
    - beautifulsoup4
    - discord.py