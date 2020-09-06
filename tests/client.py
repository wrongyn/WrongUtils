import discord
from discord.ext import commands
from WrongUtils import EmbedPaginator

client = commands.Bot(command_prefix="z.")

@client.event
async def on_ready():  
  print("I'm online!")

@client.command()
async def paginate(ctx):
  embed1 = discord.Embed(title="Page 1", description="This is page 1", color=0x00ff00)
  embed1 = discord.Embed(title="Page 2", description="This is page 2", color=0x00ff00)
  embed1 = discord.Embed(title="Page 3", description="This is page 3", color=0x00ff00)
  paginator = EmbedPaginator(ctx)
  embeds = [embed1, embed2, embed3]
  await paginator.run(embeds)

client.run(token)
