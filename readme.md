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
│  │      ................
│  │      sendmessage_discord.py
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
│      dburl.txt
│      to.txt
│
└─line
        accesstoken.txt
        to.txt
```

このようにディレクトリ/ファイルを配置すると正常に動きます。