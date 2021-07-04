from discord import Color, Embed
from discord.ext import commands
from discord.ext.commands import Cog, Context

#TODO: Connect with MLH's API

class INIT(Cog):
    """Help command and some other helper commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_withut_command=True, case_insensitive=True)
    async def init(self, ctx: Context, arg: str = None):
        if not arg:
            self.about(ctx)
        else:
            self.guild(ctx, name)

    @init.command()
    async def about(self, ctx: Context, name: str = None):
        if not arg:
            embed = Embed(title="MLH INIT 2022")
            await ctx.send(embed=embed)
        else:
            await self.guild(ctx, name)

    @init.command(aliase=["guilds"])
    async def guild(self, ctx: Context, name: str):
        await ctx.send(name)

    @init.command(aliases=["player"])
    async def mystats(self, ctx: Context):
        await ctx.send("your stats")

    @init.command()
    async def stats(self, ctx: Context, name: str = None):
        if name:
            await self.guild(name)
        else:
            await ctx.send("Some stats")

    @init.command(aliases=["id"])
    async def search(self, ctx: Context, name: str = None):
        if not name:
            await ctx.send(embed=Embed(description="Error: Name not specified", color=Color.red()))
        else:
            await ctx.send("Your info")

def setup(bot):
    bot.add_cog(INIT(bot))
