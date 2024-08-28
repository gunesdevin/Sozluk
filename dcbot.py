import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def lahmacun(ctx):
    while True:
        await ctx.send(f'https://st.depositphotos.com/2346379/2570/i/450/depositphotos_25700529-stock-photo-lahmacun.jpg')
        await ctx.send(f'LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN LAHMACUN')

bot.run("")
