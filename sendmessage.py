import requests
import json

reference="https://developers.line.biz/ja/reference/messaging-api/#send-reply-message"
with open("accesstoken.txt") as f:
    BearerToken=f.read().rstrip()

def sendmessage(to):
    with open("./messages.json") as f:
        contests=json.load(f)
    url="https://api.line.me/v2/bot/message/push"
    headers={"Content-Type":"application/json","Authorization":f"Bearer {BearerToken}"}
    message={"type":"text","text":"ぶおぶおぶお〜〜〜〜〜"}
    messages=[message]
    body={
        "to":to,
        "messages":messages,
    }
    requests.post(url,headers=headers,data=json.dumps(body))

with open("to.txt") as f:
        to=f.read().rstrip()
sendmessage(to)