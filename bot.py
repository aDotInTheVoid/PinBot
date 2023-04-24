import discord
from discord import app_commands
import os


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


@tree.command(name="pin", description="Pin a message with a message ID")
async def pin(interaction: discord.Interaction, id: str):
    channel = interaction.channel
    try:
        message = await channel.fetch_message(id)
        await message.pin()
        await interaction.response.send_message("Pinned!")
    except:
        await interaction.response.send_message("This ID seems to be invalid.")


@tree.command(name="unpin", description="Unpin a message with a message ID")
async def pin(interaction: discord.Interaction, id: str):
    channel = interaction.channel
    try:
        message = await channel.fetch_message(id)
        await message.unpin()
        await interaction.response.send_message("Unpinned!")
    except:
        await interaction.response.send_message("This ID seems to be invalid.")


client.run(os.environ["TOKEN"])
