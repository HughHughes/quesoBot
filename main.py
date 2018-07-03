# main.py runs the bot for the queso discord server which prevents discussions not about cheese
# Copyright Hugh Hughes and 1682 (2018) all rights reserved

import discord
from discord.ext import commands
import asyncio
import random

Client = discord.Client() 
client = commands.Bot(command_prefix = "?")


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord")

waPhr = []
with open('waPhr.txt') as w:
    for line in w:
        waPhr.append(line.strip('\n'))

bypass_cheese = []
with open('byCheese.txt') as b:
    for line in b:
        bypass_cheese.append(line.strip('\n'))


allowedWords = []
with open('cheeseWords.txt') as f:
    for line in f:
        allowedWords.append(line.strip('\n'))

@client.event
async def on_message(message):
    if not any(word.lower() in message.content.lower() for word in allowedWords):
        if not message.author.id in bypass_cheese:
         await client.delete_message(message)
         await client.send_message(message.author, "**Your message is not about cheese! \nTu mensaje no es sobre queso!**")

    if message.content.startswith(".cheese"):
     msg = random.choice(waPhr)
     await client.send_message(message.channel, msg)

    
    return





with open('token.txt') as t:
    token = t.readlines()
    
client.run(token[0]) 
