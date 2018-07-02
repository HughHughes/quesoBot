# main.py runs the bot for the queso discord server which prevents discussions not about cheese
# Copyright Hugh Hughes and 1682 (2018) all rights reserved

import discord
from discord.ext import commands
import asyncio

Client = discord.Client() 
client = commands.Bot(command_prefix = "?")

@client.event 
async def on_ready():
    print("Bot is online and connected to Discord")

allowedWords = []
with open('cheeseWords.txt') as f:
    for line in f:
        allowedWords.append(line.strip('\n'))

@client.event
async def on_message(message):
    if not any(word.lower() in message.content.lower() for word in allowedWords):
        await client.delete_message(message)
        await client.send_message(message.author, "**Your message is not about cheese! Tu mensaje no es sobre queso!**")
        bot_message = await client.send_message(message.channel,
                                                "Your message is not about cheese! Tu mensaje no es sobre queso!")
        await asyncio.sleep(1)
        await client.delete_message(bot_message)
    return
