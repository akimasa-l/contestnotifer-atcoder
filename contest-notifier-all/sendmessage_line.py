import requests
import json

reference = "https://developers.line.biz/ja/reference/messaging-api/#send-reply-message"
with open("../../line/accesstoken.txt") as f:
    BearerToken = f.read().rstrip()

with open("./messages.json") as f:
    contests = json.load(f)


def sendmessage(to, contest):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {BearerToken}"}
    message = {"type": "text", "text": contest}
    messages = [message]
    body = {
        "to": to,
        "messages": messages,
    }
    print(body)
    h = requests.post(url, headers=headers, data=json.dumps(body))
    print(h.text)


def gettoto():
    """
    with open("../../line/to.txt") as f:
        toto=f.read().split()
    """
    with open("../../line/dburl.txt") as f:
        dburl = f.read().rstrip()
    a = requests.get(dburl)
    toto = json.loads(a.text)
    return toto


for contest in contests:
    for to in gettoto():
        sendmessage(to, contest)
