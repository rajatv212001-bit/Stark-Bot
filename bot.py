import os
import requests
import discord
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv("DISCORD_TOKEN")


intents=discord.Intents.default()
intents.message_content=True

bot=discord.Client(intents=intents)

@bot.event
async def on_message(message):
   if message.author==bot.user:
       return
   if message.content.lower()=="hello":
       await message.channel.send("Hello Mr.Stark")
   elif message.content.lower()=="ping":
       await message.channel.send("Pong!")
   elif message.content.lower()=="$meme":
       response=requests.get("https://meme-api.com/gimme")
       data=response.json()
       await message.channel.send(data["url"])

async def on_ready():
    print(f"{bot.user} is online !")
bot.run(TOKEN)    