import discord
import asyncio
import aiohttp
import countService

@asyncio.coroutine
def returnDog(client, message):
    global tooManyRequests
    global showRequestWarning
    
    if message.channel.id == '282272609834500097' and message.content.startswith('!dog'):
        r = yield from aiohttp.get('https://random.dog/woof')
        if r.status == 200:
            text = yield from r.text()
            fileUrl = 'http://random.dog/' + text
            yield from client.send_message(message.channel, fileUrl)
