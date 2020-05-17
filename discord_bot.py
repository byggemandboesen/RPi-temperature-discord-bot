import discord
from discord.ext import commands
from gpiozero import CPUTemperature

# Sets the command prefix for calling the bot
client = commands.Bot(command_prefix = 'YOUR DESIRED COMMAND PREFIX')

# Prints (in console) when bot is ready
@client.event
async def on_ready():
    print('bot is ready!!')


# Sends RPi cpu-temp
@client.command()
async def cpu(ctx):
    cpu_read = CPUTemperature()
    await ctx.send(str(cpu_read.temperature) + ' degrees')


client.run('YOUR BOT-KEY HERE')
