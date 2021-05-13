from discord.ext import commands
import discord

base_msg = """<@267410788996743168>\n**Status Update**\n"""

def is_offline(user): return f"""\n**WARNING: {user.mention} IS NOW OFFLINE**"""

class watcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if not before.id in self.bot.watcher_cache:
            return
        print(after.name)
        if before.status != after.activity:
            print("status")
            if after.status == discord.Status.offline:
                print("offline")
                final_msg = base_msg + is_offline(after)

                channel = await self.bot.fetch_channel(self.bot.LOG_CHANNEL)
                return await channel.send(final_msg)
            else:
                final_msg = base_msg + f"{after.mention} is now {(str(after.status)).upper()}. Their old status was {(str(before.status)).upper()}"
                return await channel.send(final_msg)

def setup(bot):
    bot.add_cog(watcher(bot))