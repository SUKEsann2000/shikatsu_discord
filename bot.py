import discord
from discord import app_commands
import os
import dotenv
import subprocess

dotenv.load_dotenv()
TOKEN = os.environ["DISCORD_TOKEN"]
GUILD_ID = 1133921658034462790

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # コマンド登録
        self.tree.add_command(diag)  # 明示的に追加しないと登録されないことがある
        await self.tree.sync(guild=discord.Object(id=GUILD_ID))
        print("✅ コマンド同期完了")

client = MyClient()

@client.tree.command(name="diag", description="ラズパイの状態を表示します", guild=discord.Object(id=GUILD_ID))
async def diag(interaction: discord.Interaction):
    await interaction.response.defer(thinking=True)

    # 処理（たとえば subprocess）
    res = subprocess.run(
        ["/home/user/shikatsu/.venv/bin/python", "/home/user/shikatsu/py/start.py", "False"],
        capture_output=True,
        text=True
    )

    # 埋め込みを作成
    embed = discord.Embed(
        title="状況",
        description="ラズパイの今の情報\n\n" + res.stdout,
        colour=0x00b0f4
    )
    embed.set_author(
        name="Raspi Info",
        icon_url="https://www.wireguard.com/img/wireguard.svg"
    )
    embed.add_field(name="A New Field", value=" ", inline=False)

    # defer後なので followup.send を使う！
    await interaction.followup.send(embed=embed)

client.run(TOKEN)
