from webserver import keep_alive
import os
import discord
from discord.ext import commands
import tierlists as t
import builds as b
import runes as r
token = os.environ['token']

bot = commands.Bot(command_prefix='!')



@bot.command()
async def rune(ctx,arg1,arg2):
    r.runes(arg1,arg2)
    await ctx.send("Rünler:")
    await ctx.send(file=discord.File('runes.png'))

@bot.command()
async def tierlist(ctx):
    embed = discord.Embed(title="Tier List")
    
    embed.add_field(name= 'Top Lane Tier List' , value=t.toptierlist)

    embed.add_field(name= 'Jungle Tier List' , value=t.jungtierlist)

    embed.add_field(name= 'Mid Tier List' , value=t.midtierlist)

    embed.add_field(name= 'ADC Tier List' , value=t.adctierlist)

    embed.add_field(name= 'Support Tier List' , value=t.suptierlist)

    await ctx.send(embed=embed)


@bot.command()
async def build(ctx,arg1,arg2):
    b.items(arg1,arg2)
    await ctx.send("Başlangıç Eşyaları:")
    await ctx.send(file=discord.File('starting.png'))
    await ctx.send("Önerilen Eşyalar:")
    await ctx.send(file=discord.File('suggested.png'))


keep_alive()

bot.run(token)
