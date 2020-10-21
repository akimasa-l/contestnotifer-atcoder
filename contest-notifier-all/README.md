# contestnotifer-atcoder

コンテストの情報を見つけてLINEに送信します。

## 仕組み

毎日20時ぐらいに動かす：

1. find_contest.pyで[AtCoderのContestsサイト][1]からupcoming contestsを見る。

    - 以下のことを探す。

        - Contest name

        - Contest date

        - During time

        - Rated

        - url of contest

    - 上記をJson fileとして書き出す。

1. get_from_contest.pyで[AtCoderのPostsサイト][2]から記事を探して記事を見る。(1ページ目だけ)

    - 以下のことを探す。

        - Contest name

        - Number of problems

        - Writers

        - Points

    - 上記をJson fileとして書き出す。

1. merge.pyで上記のJson fileをContest Nameでまとめる。

    - 近いコンテストや新しいコンテストがあったらmessageを用意してsendmessage.pyを動かす。

1. sendmessage.pyで送る。

[1]:https://atcoder.jp/contests/

[2]:https://atcoder.jp/posts/
