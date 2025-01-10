import discord
from discord.ext import commands

# Bot alap konfiguráció
intents = discord.Intents.default()
intents.messages = True  # Engedélyezd az üzenetek feldolgozását

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bejelentkezve, mint {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Szia! 👋")

# Bot indítása
bot.run("MTAwMzk4ODMxODQzMTczOTkxNA.GdEYb2.o2IffxF9jpqn_ph5TX1OaoJcmua-h-lfEJF0BM")