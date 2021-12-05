import os
from dotenv import load_dotenv
from discord.ext import commands

import discord
intents = discord.Intents.default()
intents.members=True

client = discord.Client(intents=intents)

@client.event
async def on_message_join(member):
    channel = client.get_channel(524292657263017984)
    embed=discord.Embed(title=f"Welcome Ya ges yak {member.name}", description=f"Thanks for joining {member.guild.name}!") # F-Strings!
    embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
    await channel.send(embed=embed)

def main():
    babybot = commands.Bot(command_prefix="+")
    message = "Welcome"

    load_dotenv()

    @babybot.event
    async def on_ready():
        print(f"{babybot.user.name} has connected to Discord.")

    # @babybot.event
    # async def on_message(message):
    #     if (message.content.startswith("Hello")):
    #         await message.channel.send(f"Hi {message.author.mention}!")

    @babybot.command()
    async def ping(ctx):
        """Checks for a response from the bot"""
        await ctx.send("Pong")

    babybot.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()