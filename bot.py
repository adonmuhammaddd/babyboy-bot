import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

def main():
    babybot = commands.Bot(command_prefix="+")
    client = discord.Client()
    message = "Welcome"

    load_dotenv()

    @babybot.event
    async def on_ready():
        print(f"{babybot.user.name} has connected to Discord.")

    # @babybot.event
    # async def on_message(message):
    #     if (message.content.startswith("Hello")):
    #         await message.channel.send(f"Hi {message.author.mention}!")

    @client.event
    async def on_message_join(member):
        chnnel_id = 524292657263017984
        channel = client.get_channel(channel_id)
        embed=discord.Embed(title=f"Welcome Ya ges yak {member.name}", description=f"Thanks for joining {member.guild.name}!") # F-Strings!
        embed.set_thumbnail(url=member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
        await channel.send(embed=embed)

    @babybot.command()
    async def ping(ctx):
        """Checks for a response from the bot"""
        await ctx.send("Pong")

    babybot.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()