
from urllib import response
import discord
import os
import requests
import json
from arbre import *
import aiohttp

from discord.ext import commands

bot = commands.Bot(command_prefix="!")

client = discord.Client()

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)



@client.event
async def on_ready():
    print("we have logged in as{0.user}"
    .format(client))


@bot.command()
async def helpbot(ctx,arg):
    if arg !="back":
        for child in current_path[-1].list_child_node:
            if child.keyword in arg:
                current_path.append(child)
                await ctx.channel.send(child.question)
        if current_path[-1].keyword not in arg:
            await ctx.send("mettez un des mots clés émis")
            await ctx.channel.send(current_path[-1].question)
    
    elif arg == "back":
        current_path.pop()
        await ctx.channel.send(current_path[-1].question)
    
    elif arg == "quit":
        await ctx.channel.send(current_path[-1].question)
@bot.command()    
async def get_quote():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://zenquotes.io/api/random") as response:
            json_data = json.loads(await response.text())
            quote = json_data[0]["q"]
            return quote

            
@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

    
    if message.content.startswith('help'):
        await message.channel.send('comment puis je vous aider?')
    

client.run("OTgxNjAzNzIxMTczNjY3OTEw.GzKUKZ.APGICTao-qQBEj9RfY44xLEmawlLaLTPjh81HE")