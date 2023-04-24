import os
import sys

import discord
from discord import app_commands

def eprint(*args):
    print(*args, file=sys.stderr)

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")


client = aclient()
tree = app_commands.CommandTree(client)

def display_user(i: discord.Interaction):
    u = i.user.name
    return u


@tree.command(name="pin", description="PinBot: Pin a message with a message ID")
async def pin(interaction: discord.Interaction, id: str):
    channel = interaction.channel
    user = display_user(interaction)
    try:
        message = await channel.fetch_message(id)
        await message.reply(f"Pinned on behalf of {user}", mention_author=False)
        await message.pin()
        await interaction.response.send_message(f"Pinned!")
    except Exception as e:
        await interaction.response.send_message("This ID seems to be invalid.")
        eprint(e)

@tree.command(name="unpin", description="PinBot: Unpin a message with a message ID")
async def unpin(interaction: discord.Interaction, id: str):
    channel = interaction.channel
    user = display_user(interaction)
    try:
        message = await channel.fetch_message(id)
        await message.unpin()
        await message.reply(f"Unpinned on behalf of {user}", mention_author=False)
        await interaction.response.send_message(f"Unpinned!")
    except Exception as e:
        await interaction.response.send_message("This ID seems to be invalid.")
        eprint(e)

@tree.command(name="alive", description="PinBot: Has it died yet?")
async def alive(interaction: discord.Interaction):
    await interaction.response.send_message("I feel fantastic and I'm still alive")

client.run(os.environ["TOKEN"])
