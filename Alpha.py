import discord
from discord.ext import commands

import sys, traceback

def check_prefix(bot, message):
    """You get it, its prefixes"""

    prefixes = ['A-', 'Alpha-', 'A']

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

initial_extensions = ['cogs.fun',
                      'cogs.info',
                      'cogs.owner'
					  'cogs.mod']

bot = commands.Bot(command_prefix=check_prefix, description='Alpha bot')

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    await bot.change_presence(activity=discord.Game(name='Alpha | A-help', type=1, url='https://twitch.tv/dathidewolf'))
    print(f'Alpha reporting for duty!')


bot.run('')
