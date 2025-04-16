import discord
import os
import time

# Get bot token from environment variable
TOKEN = os.getenv("DISCORD_TOKEN")

# Trigger phrases that will cause the bot to reply
TRIGGER_PHRASES = ["killing myself", "kill myself", "kys", "kill yourself"]

# Path to the GIF you want to send
GIF_PATH = "nkys.gif"

# Cooldown configuration: in seconds
COOLDOWN_SECONDS = 10
user_cooldowns = {}

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

    # Debug logging
    print(f"Received message [{message.id}] from {message.author}: {message.content}")

    # Convert message to lowercase for phrase matching
    msg = message.content.lower()
    user_id = str(message.author.id)
    now = time.time()
    last_used = user_cooldowns.get(user_id, 0)

    # Check for trigger phrases and cooldown
    if any(phrase in msg for phrase in TRIGGER_PHRASES):
        if now - last_used >= COOLDOWN_SECONDS:
            user_cooldowns[user_id] = now  # Update cooldown
            if os.path.exists(GIF_PATH):
                await message.channel.send(file=discord.File(GIF_PATH))
            else:
                await message.channel.send("Oops! I can't find the GIF file.")
        else:
            print(f"Cooldown active for {message.author}, skipping response.")

client.run(TOKEN)
