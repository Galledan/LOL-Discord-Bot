from webserver import keep_alive
import os
import discord
from discord.ext import commands
import tierlists as t
import builds as b
import runes as r
import profile as p
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
async def profile(ctx,*args):
    level,kill,death,assist,profilePic,tier,flexTier,lp,flexlp,winNum,flexwinNum,loseNum,flexloseNum,tierPic,winRate,rank,flexrank,regionalRank,flexregionalRank ,champListTop5,champListRest,mainLanes = p.pro('%20'.join(args))
    
    embed = discord.Embed(title=" ".join(args), color=0x065284)
    embed.set_thumbnail(url="https:" + profilePic)

    embed.add_field(name='Seviye:', value= f"{level}", inline=False)

    embed.add_field(name='TEK/ÇİFT:', value='** **')

    embed.add_field(name='Lig:', value= f"{tier} {lp} LP", inline=False)

    embed.add_field(name='Derece:', value= f"{rank} {regionalRank.strip()}")

    embed.add_field(name='Galibiyet/Mağlubiyet:', value= f"{winNum} Galibiyet / {loseNum} Mağlubiyet", inline=False)
    
    embed.add_field(name='ESNEK', value='** **')

    embed.add_field(name= 'Lig:', value= f"{flexTier.strip()} {flexlp} LP", inline=False)

    embed.add_field(name='Derece:', value= f"{flexrank} {flexregionalRank.strip()}")

    embed.add_field(name='Galibiyet/Mağlubiyet:', value= f"{flexwinNum} Galibiyet / {flexloseNum} Mağlubiyet", inline=False)

    embed.add_field(name='-------------------------------------------', value='** **')

    embed.add_field(name='Kazanma Oranı:', value= f"{winRate}", inline=False)

    embed.add_field(name='Ortalama KDA:', value= f"{kill}/{death}/{assist}", inline=False)

    embed.add_field(name='En Çok Oynadığı Roller:', value= f"{mainLanes}", inline=False)

    embed.add_field(name='En Çok Oynadığı Şampiyonları:', value=f"{champListTop5}")

    embed.add_field(name = '** **', value=f"{champListRest}")

    
    await ctx.send(embed = embed)


@bot.command()
async def build(ctx,arg1,arg2):
    b.items(arg1,arg2)
    await ctx.send("Başlangıç Eşyaları:")
    await ctx.send(file=discord.File('starting.png'))
    await ctx.send("Önerilen Eşyalar:")
    await ctx.send(file=discord.File('suggested.png'))


keep_alive()

bot.run(token)
