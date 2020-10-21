import requests
import json
import subprocess

def make_message(a,aname,isHighest):
    diff=a["NewRating"]-a["OldRating"]
    if diff>0:
        d=2
    elif diff==0:
        d=1
    else:
        d=0
    return f"""{aname}さんの{a["ContestName"]}での成績：{a["Place"]}位
パフォーマンス：{a["Performance"]}相当
レーティング：{a["OldRating"]}→{a["NewRating"]} ({"-±+"[d] if d else ""}{diff}) :{"(|)"[d]}
{"Highestを更新しました！" if isHighest else ""}
"""
c=[]
def get_result(cname,aname):
    url=f"https://atcoder.jp/users/{aname}/history/json"
    h=json.loads(requests.get(url).text)
    a=h[-1]
    isHighest=a["NewRating"]>max(i["OldRating"]for i in h)
    if a["ContestName"]==cname:
        c.append(make_message(a,aname,isHighest))


def main():
    cname="ACL Beginner Contest"
    for aname in ("akimasa_l",):
        get_result(cname,aname)
    if c:
        with open("./messages.json",mode="w") as f:
            f.write(json.dumps(c,indent=4))
        subprocess.run("python3 ./sendmessage.py")

main()