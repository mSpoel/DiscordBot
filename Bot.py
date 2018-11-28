import discord
import asyncio
import messageBots
import settings

client = discord.Client()

@client.event
@asyncio.coroutine
def on_message(message):    
    yield from messageBots.ProcessMessage(client, message)

@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
				
client.run(settings.clientToken)
