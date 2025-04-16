import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")

TRIGGER_PHRASES = ["killing myself", "kill myself", "kys", "kill yourself", "kill your self"]

GIF_PATH = "nkys.gif"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    if any(phrase in msg for phrase in TRIGGER_PHRASES):
        if os.path.exists(GIF_PATH):
            await message.channel.send(file=discord.File(GIF_PATH))

client.run(TOKEN)
