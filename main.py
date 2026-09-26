import os
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")
bot.run(os.getenv("MTU1MzIwNzA4MDQ0MDMwNzgzNA.GD2nWy.3CJRd0BPhLwf3Y3sgMe8GdsoKD-oX4g-E-qdHM)
