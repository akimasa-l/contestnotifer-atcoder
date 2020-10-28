# contestnotifer-atcoder (in discord)

atcoder idをdiscordのグループで登録するとそのAtCoderの色にあった役職を付与します。(atcoderbot_discord.py)

あらかじめ なんとか coder という役職をサーバーに追加しておきます。(create_atcoder_role.py)

# やり方(ふだん)

※ 以下はすべて Discord の chat 欄のメッセージを示しています。

### Syntax:

```
!identify {atcoder id}
```

#### Responce:

```
{mention} は {color} coderになりました！！！
```
---

### Example

#### me:

```
!identify akimasa_l
```

#### Responce(discord-bot):

```
@Akimasa_L は green coderになりました！！！
```

## やり方(役職作成 サーバーに新しく入ってきたとき)


### me:
```
!init
```

create_atcoder_role.pyの24行目の"Akimasa_L"を別のものに変えればその人が管理者となってbotを動かすことができます。それ以外の人は使うことができません。完了したらメッセージを送れるようにしたいです。

# やり方

Ratingは`https://atcoder.jp/users/{atcoderId}/history/json`の最後のものからとってきています。とれなかったらblack coderになります。
そもそもアカウントが存在しない場合はunknown coderになります。