import time
import asyncio
import discord
import settings

counter = 0
tooManyRequests = False
oldtime = time.time()
showWarning = True

def CheckTimer():
    global tooManyRequests
    global counter
    if time.time() - oldtime > settings.intervalInSeconds:
        ResetCounters()
    if counter > settings.maxMessagesPerInterval:
        tooManyRequests = True

def ResetCounters():
    global counter
    global tooManyRequests
    global oldtime
    global showWarning
    showWarning = True
    oldtime = time.time()
    counter = 0
    tooManyRequests = False

def ShowWarning():
    global counter
    global tooManyRequests
    counter = counter + 1
    CheckTimer()
    return tooManyRequests  

@asyncio.coroutine
def ReturnWarning(client, message):
    global showWarning
    if showWarning:
        showWarning = False
        yield from client.send_message(message.channel, "too many request, please wait a moment")

    
