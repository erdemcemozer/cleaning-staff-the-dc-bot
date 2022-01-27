# @Author Erdem Özer

import os

from dotenv import load_dotenv
from discord.ext import commands
from random import randint

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


# START : BOT EVENTS
@bot.event
async def on_ready():
    print(f'{bot.user.name} is here, we actually did it boys, we connected to the server...we did it!')


# END : BOT EVENTS

# START : BOT COMMANDS
@bot.command(name='hi', help='Says you hi :D')
async def hello(ctx):
    response = 'Howdy ' + ctx.message.author.mention + "what's up with ya?"
    await ctx.send(response)


@bot.command(name='roll', help='Rolls a dice')
async def roll(ctx):
    await ctx.send(str(ctx.message.author) + " rolled and get : " + str(randint(1, 6)))


@bot.command(name='join', help='Joins the channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
        await channel.connect()


@bot.command(name='leave', help='Make the bot leave the channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


bot.run(TOKEN)
# END : BOT COMMANDS
