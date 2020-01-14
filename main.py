#Main file

import discord
import json

bot = discord.Client()
config = []
with open("config.json", "r") as f:
    config = json.load(f)
token = config["token"]

@bot.event
async def on_ready():
    print("Time to gaming.")
    print("Bot info:")
    print(bot.user.name)
    print(bot.user.id)
    print("-cool ass separator-")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.role_mentions:
        __break = 0
        for role in message.role_mentions:
            if role.name.lower() == 'every' and __break == 0:
                try:
                    await message.author.add_roles(role)
                except discord.Forbidden:
                    await message.channel.send("give me perms retard")
                __break = 1


bot.run(token)