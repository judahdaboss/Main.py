import discord
from discord.ext import commands

@bot.event
async def on_ready():
  await bot.change_presence(type=discord.ActivityType.watching, activity=discord.Game("Here"))
  
@bot.command()
async def ping(ctx):
  await ctx.send("Pong!")

bot.run(os.environ['BOT_TOKEN'])
