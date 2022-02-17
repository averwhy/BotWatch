# BotWatch
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
![GitHub last commit](https://img.shields.io/github/last-commit/averwhy/BotWatch)
![GitHub issues](https://img.shields.io/github/issues/averwhy/BotWatch)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](https://github.com/averwhy/BotWatch/compare)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

A discord bot written in discord.py that watches users statuses.

It works by caching users in a dictionary and watching for status changes based on the `on_member_update` event.

### Do note, this is very early staged code, it will be much better.


# Setup

First, create a file in the root directory named `config.py`.

Use this layout:
```py
TOKEN = '' #Bot token
LOG_CHANNEL = 00000000000000 #The channel where you want the bot to log the status changes
OWNER_ID = 00000000000000 #The ID of the owner (or the person you want pinged when a status is changed to offline)
EMBEDS = True #Whether or not to log status changes in embeds
EMBED_COLOR = 0x000280 #Can be a hex value like 0xFFFFFF or a value from the library like 'discord.Color.blue()'
COGS = ['cogs.dev', 'cogs.watcher']
```
And replace the values accordingly.

Then, to start the bot, you can start it from command line like `python bot.py`.
The bot will automatically create the database. To add bots to watch, use the