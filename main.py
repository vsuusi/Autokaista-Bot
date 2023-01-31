import discord
import os
import random
from replit import db
from keep_alive import keep_alive

client = discord.Client()

def incre(): 
  global kaista
  kaista = db["kaista_int"]
  kaista = kaista + 1
  db["kaista_int"] = kaista
  
@client.event
async def on_ready()

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("autokaista"):
    incre()
    kaistaStr = str(kaista)
    await message.channel.send("Autokaistalla käyty " + kaistaStr + " kertaa!")

keys = db.keys()
keep_alive()
token = os.environ['token']
client.run(token)



