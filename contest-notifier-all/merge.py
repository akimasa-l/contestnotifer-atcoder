# coding: utf-8
import json
import datetime
import time
import subprocess
import glob

#なんかいろいろやる
JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')
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
            ad["point"]="null"
            ad["writer"]=["null"]
            ad["problemnumber"]=["問題数：","null"]
    
    #print(*(an.items()),sep="\n")
    return an

def make_message(head,message):
    date={j:int(k)for j,k in message["date"].items()}
    cdate=datetime.datetime(date["year"], date["month"], date["day"], date["hour"], date["minute"], date["second"],tzinfo=JST)
    return head+f"""

{message["name"]} が開催されます。

コンテストページ ： {message["url"]}
開始時刻 ： {cdate.strftime('%Y-%m-%d(%a) %H:%M')}
コンテスト時間 ： {message["dtime"]["hour"]}時間 {message["dtime"]["minute"]}分
問題数： {message["problemnumber"][1]}
writer： {", ".join(message["writer"])}
レーティング変化： {message["rated"]}
{message["point"] if message["point"]!="null" else "配点：わからん"}

皆様、是非ご参加ください！"""

def get_diffs(past,now):#want name_based
    pastkeys=past.keys()
    for i in now.keys():
        if i not in pastkeys:
            messages.append(make_message("【新しいコンテストが追加されました】",now[i]))

def get_near(now,hours,head):#want original
    nowdate=datetime.datetime.now(JST)
    for i in now:
        date={j:int(k)for j,k in i["date"].items()}
        cdate=datetime.datetime(date["year"], date["month"], date["day"], date["hour"], date["minute"], date["second"],tzinfo=JST)
        if datetime.timedelta(hours=hours-1,minutes=30)<cdate-nowdate<datetime.timedelta(hours=hours,minutes=30):
            messages.append(make_message(f"【コンテスト{head}前】",i))

def search_sendmessage_py():
    path="./sendmessage_*.py"
    return glob.iglob(path)

def run_sendmessage_py(paths):
    for path in paths:
        subprocess.run("python3 "+path,shell=True)

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
    get_near(make_original(merged),1,"一時間")
    get_near(make_original(merged),24,"一日")
    if messages:
        print(f"New {len(messages)} messages are found.")
        with open("./messages.json",mode="w") as f:
            f.write(json.dumps(messages,indent=4))
        run_sendmessage_py(search_sendmessage_py())
    else:
        print("No new messages.")

main()