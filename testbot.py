import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")

bypass_cheese = []
with open('byCheese.txt') as b:
    for line in b:
        bypass_cheese.append(line.strip('\n'))

allowedWords = []
with open('cheeseWords.txt') as f:
    for line in f:
        allowedWords.append(line.strip('\n'))

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

waPhr = []
with open('waPhr.txt') as w:
    for line in w:
        waPhr.append(line.strip('\n'))

@client.command(pass_context=True)
async def cheese(context):
    msg = random.choice(waPhr)
    await client.say(msg + ", " + context.message.author.mention)

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with cheese"))
    print("Logged in as " + client.user.name)


@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())


waPhr = []
with open('waPhr.txt') as w:
    for line in w:
        waPhr.append(line.strip('\n'))

waGore = []
with open('waGore.txt') as w:
    for line in w:
        waGore.append(line.strip('\n'))

waPorn = []
with open('waPorn.txt') as w:
    for line in w:
        waPorn.append(line.strip('\n'))

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

    if message.content.startswith(".gore"):
        msg = random.choice(waGore)
        await client.send_message(message.channel, msg)

    if message.content.startswith(".porn"):
        msg = random.choice(waPorn)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!clear'):
        if message.author.id in bypass_cheese:
            tmp = await client.send_message(message.channel, 'Clearing messages...')
            async for msg in client.logs_from(message.channel):
                await client.delete_message(msg)

    if message.content.startswith('xd.png'):
        if message.author.id in bypass_cheese:
         await client.send_file(message.channel,"./xavierDolan.png")
         await client.delete_message(message)

    await client.process_commands(message)
#@client.event
#async def on_message(message):
#    if not any(word.lower() in message.content.lower() for word in allowedWords):
#        if not message.author.id in bypass_cheese:
#            await client.delete_message(message)
#            await client.send_message(message.author,
#                                      "**Your message is not about cheese! \nTu mensaje no es sobre queso!**")


with open('token.txt') as t:
    token = t.readlines()

client.run(token[0])