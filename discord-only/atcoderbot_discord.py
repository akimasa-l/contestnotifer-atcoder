import discord
import requests
import shlex
import json
import re

with open("../../discord/accesstoken.txt") as f:
    token=f.read().rstrip()

with open("../../discord/dburl.txt") as f:
    DBurl=f.read().rstrip()



client = discord.Client()

ratingcolors={1:"black",400:"gray",800:"brown",1200:"green",1600:"cyan",2000:"blue",2400:"yellow",2800:"orange",3200:"red"}

def getcolor(rating):
    for i,j in ratingcolors.items():
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

def get_atcoder_role(atcoderId,guild,discordid):
    if atcoderId:
        rating=getRating(atcoderId)
        color=getcolor(rating)
    else:#よくわからなかったら unknown coder
        rating=0
        color="unknown"
    applyDB(discordid,atcoderId,rating)
    return (discord.utils.get(guild.roles,name=color+" coder"),color)#名前で探す

async def delete_atcoder_role(member):
    delete_roles=[]
    for role in member.roles:
        if re.fullmatch("(black|gray|brown|green|cyan|blue|yellow|orange|red|unknown) coder",role.name):
            delete_roles.append(role)
    await member.remove_roles(*delete_roles)

async def sendmessage(channel,color,mention):
    reply = f'{mention} は {color} coderになりました！！！'
    await channel.send(reply)

async def add_atcoder_role(atcoderId,message):
    ok=isExist(atcoderId)
    role,color=get_atcoder_role(atcoderId if ok else "",message.guild,message.author.id)
    await message.author.add_roles(role)
    await sendmessage(message.channel,color,message.author.mention)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    a=shlex.split(message.content)
    if len(a)!=2:
        return
    if a[0]=="!identify":
        atcoderId=a[1]
        await delete_atcoder_role(message.author)
        await add_atcoder_role(atcoderId,message)

client.run(token)
