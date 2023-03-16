from discord.ext import commands

import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# create a class for my cog
class unexployed_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # To check whether the cog is loaded
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info('Audit COG loaded.')

    # Now you can add your own functionality
    @commands.command(name='sample_cmd', description='This is an example function with a check.')
    @commands.check(is_channel)
    async def sample_cmd(self, ctx):
        await ctx.send('Hello')

    # the sample_cmd only works in certain channels
    async def is_channel(ctx):   
        return ctx.channel.id in [1, 986]

async def setup(bot):
    await bot.add_cog(unexployed_cog(bot))
