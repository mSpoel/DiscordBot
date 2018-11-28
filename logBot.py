import discord
import asyncio
import configparser
import pathlib
import fnmatch
import os
import time
import datetime

def get_path(message):
    id = message.server.id
    year = datetime.date.today().year
    week = time.strftime("%U")
    return "%s/%s/%s/" % (id, year, week)

def get_filename(message):
    year = datetime.date.today().year
    week = time.strftime("%U")
    id = message.server.id
    channel = message.channel.name

    path = "%s/%s/%s/" % (id, year, week)
    file_name = "%s-%s-%s.log" % (year, week, channel)

    return path + file_name

def writeMessage(message, file):
    with open(file, "a") as f:
        # Trim the timestamp to only get [y-m-d h:m:s]
        msg = "[" + str(message.timestamp)[0:19] + "] "

        # Add author's name and padding (names are 32 chars max)
        msg += "[" + message.author.name + "] "
        for x in range(len(message.author.name), 32):
            msg += " "

        # Add author's ID and message content and write to file
        msg += "[ID: " + message.author.id + "] "
        msg += message.content
        f.write(msg + "\n")

    
@asyncio.coroutine
def logMessage(client, message):
    path = '/home/pi/Desktop/Log/'
    file = path + get_filename(message)
    try:
        writeMessage(message, file)
    except:
        os.makedirs(path + get_path(message))
        file = path + get_filename(message)
        try:
            writeMessage(message, file)
        except:
            print("Something bad happened")
