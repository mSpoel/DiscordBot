import discord
import asyncio
import random

eightBallMessages = ['It is certain',
'It is decidedly so',
'Without a doubt',
'Yes definitely',
'You may rely on it',
'As I see it, yes',
'Most likely',
'Outlook good',
'Yes',
'Signs point to yes',
'Reply hazy try again',
'Ask again later',
'Better not tell you now',
'Cannot predict now',
'Concentrate and ask again',
'Do not count on it',
'My reply is no',
'My sources say no',
'Outlook not so good',
'Very doubtful']

@asyncio.coroutine
def return8Ball(client, message):
    if message.content.startswith('!8ball'):
        yield from client.send_message(message.channel, ':8ball: ' + random.choice(eightBallMessages))
