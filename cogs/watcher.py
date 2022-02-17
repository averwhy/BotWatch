from discord.ext import commands
import discord
import config

base_msg = f"""<@{config.OWNER_ID}>\n**Status Update**\n"""

def offline(user): return f"""\n**{user.mention} is now OFFLINE.**"""

class watcher(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.checks = 0

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if not before.id in self.bot.watcher_cache:
            return
        self.checks += 1
        if before.status != after.status:
            channel = await self.bot.fetch_channel(self.bot.LOG_CHANNEL)
            if after.status == discord.Status.offline:
                final_msg = offline(after)
            else:
                final_msg = f"{after.mention} is now {(str(after.status)).upper()}. Their old status was {(str(before.status)).upper()}"
            
            if config.EMBEDS: return await channel.send(content=base_msg, embed=discord.Embed(description=final_msg, color=config.EMBED_COLOR))
            else: return await channel.send(base_msg + final_msg)

def setup(bot):
    bot.add_cog(watcher(bot))