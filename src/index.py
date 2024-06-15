import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True
bot = commands.Bot(command_prefix=".", intents=permissoes)


load_dotenv(dotenv_path='C:\\Users\\user\\Documents\\python\\coffebotmusic\\.env')
ID = os.getenv('ID')
TOKEN = os.getenv('TOKEN')


@bot.event
async def on_ready():
    print('Estou pronto!')

@bot.command()
async def ola(ctx):
   await ctx.reply('olá')

bot.run(TOKEN)


