from discord.ext import commands
import discord
import typing

class dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if not guild.id in self.bot.server_whitelist:
            await guild.leave()

    async def cog_check(self, ctx): # Makes this cog's commands owner only
        return ctx.author.id == self.bot.owner_id

    @commands.command()
    async def add(self, ctx, bot: typing.Union[discord.User, discord.Member]):
        """adds a bot to the watchlist"""
        if not bot.bot and bot.id == self.bot.owner_id:
            return await ctx.send("thats not a bot \:(")
        try:
            await self.bot._register_bot(bot.id)
            return await ctx.send(":slight_smile: \U0001f44d")
        except Exception as e:
            return await ctx.send(f":pensive:\n{e}")

    @commands.command()
    async def watching(self, ctx):
        bots = "\n".join(f"<@{str(b)}>" for b in self.bot.watcher_cache) # `join` wont work with ints, so make string using this cool one liner
        await ctx.send(f"Watchlist: \n{bots}")

def setup(bot):
    bot.add_cog(dev(bot))