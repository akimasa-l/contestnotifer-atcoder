import discord
import requests
import json

with open("../../discord/accesstoken.txt") as f:
    token=f.read().rstrip()

client = discord.Client()

color={0:"gray",400:"brown",800:"green",1200:"cyan",1600:"blue",2000:"yellow"}

async def getcolor(atcoderId):
    url=f"https://atcoder.jp/users/{atcoderId}/history/json"
    a=requests.get(url)
    d=json.loads(a.text)
    if d:
        pass
    else:
        return "black"

async def isExist(atcoderId):
    url=f"https://atcoder.jp/users/{atcoderId}/"
    a=requests.get(url)
    if a.status_code==200:
        return True
    return False

@client.event
async def on_message(message):
    if message.author.bot:
        return
    a=message.content.split()
    if len(a)!=2:
        return
    if a[0]=="!identify":
        await isExist(a[1])

client.run(token)
