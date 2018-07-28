import asyncio
from discord.ext.commands import Bot

client = Bot(command_prefix='!')

@client.command(pass_context=True)
async def ping():
    await client.say('pong')

@client.event
async def on_message():
    pass

with open('token.txt') as t:
    token = t.readlines()
client.run(token[0])