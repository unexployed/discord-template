import nextcord
from nextcord.ext import commands

import os
import asyncio
import logging

discord_bot_token = ""
application_id = ""

intents = nextcord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents, application_id=application_id)

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

@bot.event
async def on_ready():
    # Check if bot is online
    logging.info('Online.')


async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    # loads cogs before starting
    await load()
    await bot.start(discord_bot_token)

asyncio.run(main())
