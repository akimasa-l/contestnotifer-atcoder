import discord
import requests
import shlex
import json
import re
import aiohttp

with open("../../discord/accesstoken.txt") as f:
    token=f.read().rstrip()

with open("../../discord/dburl.txt") as f:
    DBurl=f.read().rstrip()

with open("../../discord/channelid.txt") as f:
    channelid=int(f.read().rstrip())

client = discord.Client()

ratingcolors={1:"black",400:"gray",800:"brown",1200:"green",1600:"cyan",2000:"blue",2400:"yellow",2800:"orange",10000:"red"}

async def getcolor(rating)->str:
    for i,j in ratingcolors.items():
        if rating<i:
            return j

async def applyDB(discordid,atcoderid,rating):
    params={"discordid":discordid,"atcoderid":atcoderid,"rating":rating}
    async with aiohttp.ClientSession() as session:
        async with session.post(DBurl,params) as r:
            j=json.loads(await r.text())
    #a=requests.post(DBurl,params=params)
    return j

async def getRating(atcoderId)->int:
    url=f"https://atcoder.jp/users/{atcoderId}/history/json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            j=json.loads(await r.text())
    if j:
        return j[-1]["NewRating"]
    return 0

async def get_discord_id_dict_by_DB()->dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(DBurl) as r:
            j=json.loads(await r.text())
    return j

async def isExist(atcoderId)->bool:
    url=f"https://atcoder.jp/users/{atcoderId}/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            if r.status==200:
                return True
    #a=requests.get(url)
    return False

async def get_atcoder_role(atcoderId,guild,discordid):
    if atcoderId:
        rating=await getRating(atcoderId)
        color=await getcolor(rating)
    else:#よくわからなかったら unknown coder
        rating=0
        color="unknown"
    await applyDB(discordid,atcoderId,rating)
    return (discord.utils.get(guild.roles,name=color+" coder"),color)#名前で探す

async def delete_atcoder_roles(member):
    delete_roles=[]
    compiled=re.compile("(black|gray|brown|green|cyan|blue|yellow|orange|red|unknown) coder")
    for role in member.roles:
        if compiled.fullmatch(role.name):
            delete_roles.append(role)
    await member.remove_roles(*delete_roles)#unpackする

async def sendmessage(channel,color,mention):
    reply = f'{mention} は {color} coderになりました！！！'
    await channel.send(reply)

async def add_atcoder_role(atcoderId,channel,user):
    ok=await isExist(atcoderId)
    role,color=await get_atcoder_role(atcoderId if ok else "",channel.guild,user.id)
    await user.author.add_roles(role)
    await sendmessage(channel,color,user.mention)

async def get_user_for_discord_id(discordId,members):
    #https://discordpy.readthedocs.io/ja/latest/api.html?highlight=find#discord.utils.find
    return discord.utils.find(lambda m:str(m.id)==str(discordId),members)

async def update_user_role(atcoderId,channel,user):
    await delete_atcoder_roles(user)
    await add_atcoder_role(atcoderId,channel)

async def update_users_role(channel):
    j=get_discord_id_dict_by_DB()
    for discordId in j.keys():
        user=await get_user_for_discord_id(discordId,channel.guild.members)
        await update_user_role(j[discordId]["atcoderId"],channel,user)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    a=shlex.split(message.content)
    if len(a)!=2:
        return
    atcoderId=a[1]
    if a[0]=="!identify":
        await update_user_role(atcoderId,message.channel,message.author)
    if a[0]=="!update":
        await update_users_role(message.channel)

@client.event
async def on_ready():
    channel=client.get_channel(channelid)
    await update_users_role(channel)

client.run(token)
