import discord
import asyncio
import aiohttp
import countService

@asyncio.coroutine
def returnCat(client, message):
    global tooManyRequests
    global showRequestWarning
	
    if message.channel.id == '282272609834500097' and message.content.startswith('!cat'):
        r = yield from aiohttp.get('http://random.cat/meow')
        if r.status == 200:
            js = yield from r.json()
            yield from client.send_message(message.channel, js['file'])
