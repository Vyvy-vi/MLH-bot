from discord import Color, Embed
from discord.ext import commands
from discord.ext.commands import Cog, Context
from aiohttp import ClientSession

#TODO: Connect with MLH's API

async def call_api(url: str):
    async with ClientSession() as session:
        async with session.get("https://init-leadboard.web.app/" + url) as response:
            return await response.json()

class INIT(Cog):
    """Help command and some other helper commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def init(self, ctx: Context, arg: str = None):
        await self.about(ctx, arg)

    @init.command()
    async def about(self, ctx: Context, name: str = None):
        if not name:
            embed = Embed(
                title="MLH INIT 2022",
                description="INIT is a celebration for the start of the 2022 Hackathon Season! \
While this is the first time we are running INIT, the format will feel familiar to those who \
have participated in Local Hack Day. You can expect to complete challenges, \
hear about BIG community announcements, chat at hacker hangouts, enjoy fun \
live sessions, and make new memories (and memes).\n\n\
[**Attend INIT**](https://organize.mlh.io/participants/events/6813-init-2022)\
",
                url="https://init.mlh.io/",
                color=0x1d1a4f)
            embed.add_field(
                name="**Sponsors**",
                value="MLH couldn’t run INIT without the support of our incredible partners. \
Check back here for more information to come!\n\
**.tech Domains** | **xylem** | **replit** | **jina**")
            embed.set_author(
                name="Major League Hacking",
                icon_url="https://cdn.discordapp.com/emojis/697961542775472198.png?v=1",
            )
            await ctx.send(embed=embed)
        else:
            await self.guild(ctx, name)

    @init.command(aliase=["guilds"])
    async def guild(self, ctx: Context, name: str):
        if not name:
            await ctx.send("This is the current guild leaderboard")
        else:
            await ctx.send("This isn't directly query-able, and I am not a fan of looping over things")

    @init.command(aliases=["player"])
    async def mystats(self, ctx: Context):
        await ctx.send("your stats")

    @init.command()
    async def stats(self, ctx: Context, name: str = None):
        if name:
            await self.guild(ctx, name)
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
