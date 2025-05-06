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

client.run(TOKEN)
