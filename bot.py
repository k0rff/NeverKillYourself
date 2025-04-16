import discord
import os

# Replace this with your bot token
TOKEN = 'TOKENHERE'

# Phrase to trigger the video reply
TRIGGER_PHRASE = "kill myself"
# Path to the video you want to send (make sure this file exists)
VIDEO_PATH = "nkys.gif"

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

    if TRIGGER_PHRASE in message.content.lower():
        if os.path.exists(VIDEO_PATH):
            await message.channel.send(file=discord.File(VIDEO_PATH))
        else:
            await message.channel.send("Sorry, the video file is missing!")

client.run(TOKEN)
