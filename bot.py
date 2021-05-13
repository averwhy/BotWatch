from discord.ext import commands
import discord
import aiosqlite
import config
import traceback
import asyncio, os
from datetime import datetime

def get_pre(bot, message):
    # epic variable name
    _ = '' if message.author.id == bot.owner_id else '<'
    return _

class BotWatch(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    async def _register_bot(self, botid: int):
        await self.db.execute("INSERT INTO bots VALUES (?, ?)", (botid, datetime.utcnow()))
        self.watcher_cache.append(botid)
        await self.db.commit()


bot = BotWatch(command_prefix=get_pre, intents=discord.Intents.all())

async def launch(bot):
    bot.db = await aiosqlite.connect('bw.db')
    await bot.db.execute("CREATE TABLE IF NOT EXISTS bots (id int, watchingsince blob)")

    bot.LOG_CHANNEL = config.LOG_CHANNEL
    bot.server_whitelist = [724456699280359425]

    cur = await bot.db.execute("SELECT id FROM bots")
    bot.watcher_cache = [bots for bots in await cur.fetchall()]

asyncio.run(launch(bot))
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True" 
os.environ["JISHAKU_HIDE"] = "True"
for c in config.COGS:
    try:
        bot.load_extension(c)
    except Exception:
        print(traceback.format_exc())

@bot.event
async def on_ready():
    print(f"{str(bot.user)} is connected")
    print('-' * 20)

bot.run(config.TOKEN)