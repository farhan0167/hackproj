import os

import discord
#from dotenv import load_dotenv

#load_dotenv()
TOKEN = "MTA3NjYyNjAxMjM5NTI3NDI2MA.G5EyU6.RBj6Ykm1AbyJmxnrS7RuF4edcD7ZIMx_YbHt0M"
GUILD = "1076626797061488640"


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!query':
        #https://stackoverflow.com/questions/71797750/how-to-send-message-in-a-discord-thread
        thread = await message.channel.create_thread(name="Thread" , type=discord.ChannelType.public_thread )
        await thread.send("This message is sent to the created thread!")

client.run(TOKEN)
