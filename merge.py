# coding: utf-8
import json
import datetime
import time
import subprocess

#なんかいろいろやる

messages=[]

def make_name_based_object(a):
    return {i["name"]:i for i in a}

def make_original(a):
    return a.values()

def merge_contests_and_posts(contests,posts):
    a=contests
    b=posts
    #json.loads("upcomingじゃなくてposts")
    
    an=make_name_based_object(a)
    bn=make_name_based_object(b)
    bnkeys=bn.keys()
    for i in an.keys():
        ad=an[i]
        if i in bn:
            bd=bn[i]
            for j in ("writer","problemnumber","point"):
                ad[j]=bd[j]
        else:
            for j in ("problemnumber","point"):
                ad[j]="null"
            ad["writer"]=[]
    
    #print(*(an.items()),sep="\n")
    return an

def make_message(flag,message):
    date=message["date"]
    cdate=datetime(date["year"], date["month"], date["day"], date["hour"], date["minute"], date["second"], date["microsecond"],tzinfo="JST")
    head="【新しいコンテストが追加されました】"if flag else "【コンテスト一時間前】"
    return head+f"""

{message["name"]} が開催されます。

コンテストページ ： {message["url"]}
開始時刻 ： {cdate.strftime('%Y-%m-%d(%a) %H:%M')}
コンテスト時間 ： {message["dtime"]["hour"]}時間 {message["dtime"]["minute"]}分
問題数： {message["problemnumber"]}
writer： {", ".join(message["writer"])}
レーティング変化： {message["rated"]}
配点は {message["point"]} です。

皆様、是非ご参加ください！"""

def get_diffs(past,now):#want name_based
    pastkeys=past.keys()
    for i in now.keys():
        if i not in pastkeys:
            messages.append(make_message(1,now[i]))

def get_near(now):#want original
    JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
    nowdate=datetime.datetime.now(JST)
    for i in now:
        date={j:int(k)for j,k in i["date"].items()}
        cdate=datetime.datetime(date["year"], date["month"], date["day"], date["hour"], date["minute"], date["second"],tzinfo=JST)
        if cdate-nowdate<datetime.timedelta(hours=1,minutes=30):
            messages.append(make_message(0,i))

def main():
    with open("./merged.json") as f:
        past=json.load(f)
    with open("./find_contest.json") as f:
        contests=json.load(f)
    with open("./get_from_posts.json") as f:
        posts=json.load(f)
    merged=merge_contests_and_posts(contests,posts)
    with open("./merged.json",mode="w") as f:
        f.write(json.dumps(merged,indent=4))
    get_diffs(past,merged)
    get_near(make_original(merged))
    if messages:
        with open("./messages.json",mode="w") as f:
            f.write(json.dumps(messages,indent=4))
        subprocess.run("python3 ./sendmessage.py")
main()