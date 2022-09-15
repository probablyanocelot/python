# required packages: discord.py, python_dotenv
# This example requires the 'messages' intent and 'manage messages' bot permission.
# Comment print lines for true purities
# create '.env' file in this file's root dir & write: DISCORD_TOKEN='my_bots_private_token'
# RESOURCES: https://discordpy.readthedocs.io/en/stable/#getting-started


import discord
import asyncio
from random import choice
from os import getenv
from dotenv import load_dotenv

load_dotenv()


channels = {
    'cannabois': 799211146301145088,
}


THANOS = False
RESPOND = False

DISCORD_TOKEN = getenv("DISCORD_TOKEN_CORN")
MESSAGE_LIFE = 25.0  # time, in seconds, before message is wiped
THANOS_CHANNELS = ['uwu-job-larping', 'general', ]

RESPONSE_LIST = ['orly?', 'lmao, riiight...', 'yeah - tell us more, scrub', ]


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # displays only author if no message.content intent
        print(f'Message from {message.author}: {message.content}')

        if RESPOND:
            await self.bully(message)

        if THANOS:
            await self.timed_delete(message)

    async def bully(self, message):
        if not str(message.channel) in THANOS_CHANNELS:
            return
        if str(message.author) == 'cOrn $queezer#1278':
            return
        if str(message.author) == 'FAil Boat#2414':
            await message.channel.send("shhh, only corn can make bot thx... jk, you should try. he will help")
            return
        print('we gonna fuckin bully {}'.format(message.author))
        # channel = client.get_channel(id=message.channel.id)
        await message.channel.send(choice(RESPONSE_LIST))

    async def timed_delete(self, message):
        # channel = discord.utils.get(message.guild.channels, name=given_name)
        # channel_id = channel.id
        print(message.channel.id)
        if not str(message.channel) in THANOS_CHANNELS:
            return
        if not str(message.author) == 'Cornboi#0146':  # 'cOrn $queezer#1278' or
            return
        print('waiting {}s to delete message from {}'.format(
            MESSAGE_LIFE, message.author))
        await asyncio.sleep(MESSAGE_LIFE)
        print('deleting message')
        await message.delete()

    async def self_delete(self, message):
        pass


intents = discord.Intents.default()
intents.messages = True

client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
