#API reference
#https://discordpy.readthedocs.io/ja/latest/api.html?highlight=role#discord.Guild.create_role
import discord
import configparser

config=configparser.ConfigParser()
with open("./colors.ini") as f:
    config.read_file(f)

with open("../../discord/accesstoken.txt") as f:
    token=f.read().rstrip()

#print(config["colors"].items())
client = discord.Client()



client.run(token)