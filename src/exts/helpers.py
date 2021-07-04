from discord.ext import commands
from discord.ext.commands import Cog, Context

from src.consts import META


class Helpers(Cog):
    """Help command and some other helper commands"""

    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("Bot is online! Currently running version - v%s" % META["version"])

    @commands.command()
    async def ping(self, ctx: Context):
        await ctx.send("Pong! Running version - v%s" % META["version"])

def setup(bot):
    bot.add_cog(Helpers(bot))
