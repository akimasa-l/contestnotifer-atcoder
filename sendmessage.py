import requests
import json

reference="https://developers.line.biz/ja/reference/messaging-api/#send-reply-message"
with open("../accesstoken.txt") as f:
    BearerToken=f.read().rstrip()

with open("./messages.json") as f:
    contests=json.load(f)

def sendmessage(to,contest):
    url="https://api.line.me/v2/bot/message/push"
    headers={"Content-Type":"application/json","Authorization":f"Bearer {BearerToken}"}
    message={"type":"text","text":contest}
    messages=[message]
    body={
        "to":to,
        "messages":messages,
    }
    print(body)
    h=requests.post(url,headers=headers,data=json.dumps(body))
    print(h.text)

with open("../to.txt") as f:
    to=f.read().rstrip()

for contest in contests:
    sendmessage(to,contest)