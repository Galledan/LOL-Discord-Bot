from webserver import keep_alive
import os
import discord
from discord.ext import commands
import tierlists as t
token = os.environ['token']

bot = commands.Bot(command_prefix='!')


@bot.command()
async def pick(ctx, arg1, arg2):
    await ctx.send('https://www.op.gg/champion/{}/statistics/{}'.format(arg1, arg2))

@bot.command()
async def counter(ctx, arg1, arg2):
    await ctx.send('https://tr.op.gg/champion/{}/statistics/{}/matchup'.format(arg1, arg2))

@bot.command()
async def build(ctx, arg1, arg2):
    await ctx.send('https://tr.op.gg/champion/{}/statistics/{}/item'.format(arg1, arg2))

@bot.command()
async def rune(ctx, arg1, arg2):
    await ctx.send('https://www.op.gg/champion/{}/statistics/{}/rune'.format(arg1, arg2))

@bot.command()
async def opgg(ctx, arg1):
    await ctx.send('https://tr.op.gg/summoner/userName={}'.format(arg1))

@bot.command()
async def tierlist(ctx):
    embed = discord.Embed(title="Tier List")
    
    embed.add_field(name= 'Top Lane Tier List' , value=t.toptierlist)

    embed.add_field(name= 'Jungle Tier List' , value=t.jungtierlist)

    embed.add_field(name= 'Mid Tier List' , value=t.midtierlist)

    embed.add_field(name= 'ADC Tier List' , value=t.adctierlist)

    embed.add_field(name= 'Support Tier List' , value=t.suptierlist)

    await ctx.send(embed=embed)


keep_alive()

bot.run(token)
