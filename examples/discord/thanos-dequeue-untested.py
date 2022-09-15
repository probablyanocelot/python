from time import time
from collections import deque
import discord
import asyncio
from os import getenv
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = getenv("DISCORD_TOKEN")
MESSAGE_LIFE = 86400  # time, in seconds, before message is wiped
THANOS_CHANNELS = ['uwu-job-larping', ]
toDelete = Queue()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if not str(message.channel) in THANOS_CHANNELS:
            return
        toDelete.put((time()+MESSAGE_LIFE, message))


intents = discord.Intents.default()
intents.messages = True

client = MyClient(intents=intents)


@tasks.loop(seconds=30)
async def deleter():
    while True:
        t, m = toDelete[0]
        if t > time():
            break
        await m.delete()
        toDelete.popleft()


@deleter.before_loop
async def bl_deleter():
    await client.wait_until_ready()

deleter.start()
client.run(DISCORD_TOKEN)
