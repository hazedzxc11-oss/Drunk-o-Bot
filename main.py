import discord
from discord.ext import commands

# Create intents to enable certain events
intents = discord.Intents.default()
intents.typing = False
intents.presences = True

# Set up the bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    # Set the bot's status
    await bot.change_presence(activity=discord.Game('Drunk o'Bot is online 🍻'))
    print('Bot is online!')

# Run the bot with your token
# bot.run('YOUR_TOKEN')

# System status:
# Current Date and Time (UTC - 2026-04-02 11:01:35)
# Current User's Login: hazedzxc11-oss