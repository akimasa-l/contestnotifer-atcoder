import requests
import json

reference = "https://developers.google.com/hangouts/chat/how-tos/webhooks"
with open("./messages.json") as f:
    contests = json.load(f)


def sendmessage(to, contest):
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    body = {"text": contest}
    # print(body)
    h = requests.post(to, headers=headers, data=json.dumps(body))
    # print(h.text)


with open("../../google_chat/to.txt") as f:
    toto = f.read().split()

for contest in contests:
    for to in toto:
        sendmessage(to, contest)
