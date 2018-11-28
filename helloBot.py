import discord
import asyncio

@asyncio.coroutine
def returnHello(client, message):
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        yield from client.send_message(message.channel, msg) 
