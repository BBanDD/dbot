import discord
import os


client = discord.Client()

@client.event
async def on_ready():

  print("login")
  print(client.user.name)
  print("------------------")
  await client.change_presence(game=discord.gmae(name=' ', type=1))

@client.event
async def on_message(message):
  if Message.contect.startswith("hi")
      await client.send_message(message.channel, "your mom")
    
    
    
    
access_token = os.environ["Bot_TOKEN"]
client.run(access_token)
