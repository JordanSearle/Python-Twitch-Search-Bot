import os
import test
from test import chatbot_query

import sys
sys.path.append('c:/users/jorda/appdata/local/programs/python/python38-32/lib/site-packages')

from twitchio.ext import commands

irc_token='oauth:#####'
client_id='#####'
nick='#####'
prefix='!'
initial_channels=['#####']

print(chatbot_query)
# set up the bot
bot = commands.Bot(
    irc_token=irc_token,
    client_id=client_id,
    nick=nick,
    prefix=prefix,
    initial_channels=initial_channels
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    #print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(initial_channels[0], f"/me has landed!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == nick.lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    #if ctx.author.name.lower() == "cornishmadman":
    #        await ctx.channel.send(ctx.content)
    print(ctx)        
    
    #if 'cornish' in ctx.content.lower() and ctx.author.name == "cornishmadman":        
    #    await ctx.channel.send(f"Hi, @{ctx.author.name}!")
        
    #if 'cookiee' in ctx.content.lower() and ctx.author.name == "cornishmadman":        
    #    await ctx.channel.send(f"!salt")
    if '?' in ctx.content.lower():
        t = chatbot_query(str(ctx.content))
        await ctx.channel.send(t)
    
@bot.command(name='cookiee')
async def test(ctx):
    await ctx.send('!salt')


if __name__ == "__main__":
    bot.run()
