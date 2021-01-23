import json
import requests

with open("../../discord/to.txt") as f:
    urls = f.read().split()

with open("./messages.json") as f:
    contests = json.load(f)


def sendmessage(url, message):
    params = {
        "content": message,
    }
    headers = {"Content-Type": "application/json"}
    a = requests.post(url, data=json.dumps(params), headers=headers)
    print(a.status_code)
    print(a.text)


if __name__ == "__main__":
    for url in urls:
        for contest in contests:
            sendmessage(url, contest)
