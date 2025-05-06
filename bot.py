import discord
from discord import app_commands
import os
import dotenv

dotenv.load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]#環境変数からトークンを取得

intents = discord.Intents.default()#適当に。
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("起動完了")
    await tree.sync()#スラッシュコマンドを同期

@tree.command()
async def diag(interaction: discord.Interaction):
    embed = discord.Embed(title="状況",
                      description="ラズパイの今の情報\n\nここにoutputを書く",
                      colour=0x00b0f4)

    embed.set_author(name="Raspi Info",
                 icon_url="https://www.wireguard.com/img/wireguard.svg")

    embed.add_field(name="A New Field",
                value="",
                inline=False)

    await interaction.response.send_message(embed=embed)

client.run(TOKEN)
