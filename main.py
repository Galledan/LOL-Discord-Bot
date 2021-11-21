import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

coms = """Komutlar: opgg, pick, counter, build, rune
Yazılış:!komut şampiyonismi lane
"""

@bot.command()
async def commands(ctx):
    await ctx.send(coms)

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

bot.run('token')
