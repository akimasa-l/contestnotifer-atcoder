import requests
import json

reference="https://developers.line.biz/ja/reference/messaging-api/#send-reply-message"

BearerToken=""

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

sendmessage("to")