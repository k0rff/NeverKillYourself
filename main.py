import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")

TRIGGER_PHRASES = ["killing myself", "kill myself", "kys", "kill yourself"]

GIF_PATH = "nkys.gif"

# Set up the bot with necessary intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Prevent bot from responding to itself
    if message.author == client.user:
        return

    # Convert message content to lowercase and check for any trigger phrase
    msg = message.content.lower()
    if any(phrase in msg for phrase in TRIGGER_PHRASES):
        if os.path.exists(GIF_PATH):
            await message.channel.send(file=discord.File(GIF_PATH))

client.run(TOKEN)
