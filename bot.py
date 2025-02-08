import discord
from discord.ext import commands
from bot.config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.load_extension('bot.commands.geoguess')  # Await the load_extension call

bot.run(DISCORD_TOKEN)