#API reference
#https://discordpy.readthedocs.io/ja/latest/api.html?highlight=role#discord.Guild.create_role
import discord
import configparser

config=configparser.ConfigParser()
with open("./colors.ini") as f:
    config.read_file(f)

colors={i:discord.Color(int(j,16)) for i,j in config["colors"].items()}

#print(*colors.values())

with open("../../discord/accesstoken.txt") as f:
    token=f.read().rstrip()

#print(config["colors"].items())

client = discord.Client()



client.run(token)