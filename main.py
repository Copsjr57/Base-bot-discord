import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Discord token from environment variables
TOKEN = os.getenv('DISCORD_TOKEN')

# Check if token is defined
if TOKEN is None:
    print("Error: Discord token not defined in .env file")
    exit(1)

# Create bot instance with command prefix '!'
# Intents are required for certain functionalities
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to read message content

bot = commands.Bot(command_prefix='!', intents=intents)

# Flag to load cogs only once
cogs_loaded = False

async def load_cogs():
    """
    Load all cogs (extensions) for the bot.
    """
    global cogs_loaded
    if cogs_loaded:
        return
    
    try:
        await bot.load_extension('help_cog')
        await bot.load_extension('general')
        await bot.load_extension('moderation')
        await bot.load_extension('channels')
        cogs_loaded = True
        print("All cogs loaded successfully!")
    except Exception as e:
        print(f"Error loading cogs: {e}")

@bot.event
async def on_ready():
    """
    Event triggered when the bot is ready and connected to Discord.
    """
    print(f'Bot connected as {bot.user}')
    print('Ready to receive commands!')
    await load_cogs()  # Load cogs after connection

# Error handling
@bot.event
async def on_command_error(ctx, error):
    """
    Error handler for commands.
    """
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command. Use `!help` to see available commands.")
    else:
        print(f"Error: {error}")

# Lancer le bot
if __name__ == "__main__":
    bot.run(TOKEN)