import discord
from discord.ext import commands, tasks
import asyncio

# Botのインスタンスを作成
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# リマインド機能のコマンドを定義
@bot.command(name='remind')
async def remind(ctx, time: int, *, message: str):
    # 特定のチャンネルのIDを設定
    CHANNEL_ID = 839474364390965322  # ここにチャンネルIDを入力

    # ギルド（サーバー）からチャンネルを取得
    channel = ctx.guild.get_channel(CHANNEL_ID)

    if channel is not None:
        await ctx.send(f'リマインドを設定しました。{time}秒後にリマインドします。')
        await asyncio.sleep(time)
        await channel.send(f'リマインド: {message}')
    else:
        await ctx.send("指定されたチャンネルが見つかりませんでした。")


# Botをログアウトさせるコマンド
@bot.command(name='logout')
@commands.is_owner()  # このデコレーターを使うと、ボットのオーナーのみがこのコマンドを実行できるようになります
async def logout(ctx):
    await ctx.send("ログアウトします。")
    await bot.close()  # Botをログアウト（接続解除）させる

# Botが起動したときの処理
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


# Discordのトークンを使用してBotを実行
bot.run('Token')
