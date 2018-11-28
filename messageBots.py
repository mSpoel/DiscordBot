import discord
import asyncio
import logBot
import eightballBot
import helloBot
import catBot
import dogBot
import countService
import settings

@asyncio.coroutine
def ProcessMessage(client, message):
    if settings.useLogging:
        yield from logBot.logMessage(client, message)
    
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if message.content.startswith(tuple(restrictedCommands)):
        if countService.ShowWarning():
            yield from countService.ReturnWarning(client, message)
        else:
            yield from ProcessRestrictedMessages(client, message) 
			
restrictedCommands = ['!cat', '!dog',  '!8ball']
			
@asyncio.coroutine
def ProcessRestrictedMessages(client, message): 
    yield from catBot.returnCat(client, message)
    yield from dogBot.returnDog(client, message)
    yield from eightballBot.return8Ball(client, message)
    yield from helloBot.returnHello(client, message)	



