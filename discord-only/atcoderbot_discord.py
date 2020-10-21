import discord
import requests
import shlex
import json

with open("../../discord/accesstoken.txt") as f:
    token=f.read().rstrip()

with open("../../discord/dburl.txt") as f:
    DBurl=f.read().rstrip()



client = discord.Client()

colors={1:"black",400:"gray",800:"brown",1200:"green",1600:"cyan",2000:"blue",2400:"yellow",2800:"orange",3200:"red"}

def getcolor(rating):
    for i,j in colors.items():
        if rating<i:
            return j

def applyDB(discordid,atcoderid,rating):
    params={"discordid":discordid,"atcoderid":atcoderid,"rating":rating}
    a=requests.post(DBurl,params=params)
    return json.dumps(a.text)

def getRating(atcoderId)->int:
    url=f"https://atcoder.jp/users/{atcoderId}/history/json"
    a=requests.get(url)
    j=json.loads(a.text)
    if j:
        return j[-1]["NewRating"]
    return 0


def isExist(atcoderId):
    url=f"https://atcoder.jp/users/{atcoderId}/"
    a=requests.get(url)
    if a.status_code==200:
        return True
    return False

@client.event
async def on_message(message):
    if message.author.bot:
        return
    a=shlex.split(message.content)
    if len(a)!=2:
        return
    if a[0]=="!identify":
        ok=await isExist(a[1])
        if ok:
            pass

client.run(token)
