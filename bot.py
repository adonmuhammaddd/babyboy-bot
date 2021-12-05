import os
from dotenv import load_dotenv
from discord.ext import commands

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

    @babybot.event
    async def on_member_join(member):
        channel = get(member.server.channels, name="general")
        await babybot.send_message(channel,"welcome") 

    # @babybot.event
    # async def on_member_join(member):
    #     for channel in babybot.get_all_channels():
    #         if channel.name == 'kuntul':
    #             await channel.send(
    #                 f'Hi {member.mention}, Message to send when member joins')

    @babybot.command()
    async def ping(ctx):
        """Checks for a response from the bot"""
        await ctx.send("Pong")

    babybot.run(os.getenv("DISCORD_TOKEN"))

if __name__ == '__main__':
    main()