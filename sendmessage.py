import requests
import json

reference="https://developers.line.biz/ja/reference/messaging-api/#send-reply-message"

BearerToken=""

def sendmessage(to):
    url="https://api.line.me/v2/bot/message/push"
    headers={"Content-Type":"application/json","Authorization":f"Bearer {BearerToken}"}
    message={"type":"text","text":"ぶおぶおぶお〜〜〜〜〜"}
    messages=[message]
    requests.post(url=url,header=headers,params=messages)