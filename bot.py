import os

import discord
#from dotenv import load_dotenv

#load_dotenv()
TOKEN = ""
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

"""def format(threadMessages):
    for i in range(threadMessages):
        if i == 0:
            prepend with Q:
        else if i%2 == 0:
            prepend with A:
        else prepend with Q:
    
    return

    return Q/A format
def deal(message, thread):

    formattedThread = format(thread)
    # response = make a get request, with parameter formattedThread
    response = formattedThread
    return response"""

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!query') and message.channel.name == 'general':
        print(message)
        print("channel")
        #https://stackoverflow.com/questions/71797750/how-to-send-message-in-a-discord-thread
        thread = await message.channel.create_thread(name="Thread" , type=discord.ChannelType.public_thread )
        await thread.send("This message is sent to the created thread!")
        #deal(message, thread_messages)
    elif message.content.startswith('!query') and message.channel.name != 'general':
        print(message)
        print("thread")
        thread_id = message.channel.id
        thread = message.guild.get_thread(thread_id)
        msg = "Message within a thread"
        await thread.send("This message is sent within the thread!")
            

client.run(TOKEN)


"""
<Message id=1076648261777105017 channel=<TextChannel id=1076626797061488644 name='general' position=0 
nsfw=False news=False category_id=1076626797061488641> type=<MessageType.default: 0> author=<Member 
id=881987116635160596 name='fenderbender' discriminator='5706' bot=False nick=None guild=<Guild 
id=1076626797061488640 name="fenderbender's server" shard_id=0 chunked=False member_count=3>> 
flags=<MessageFlags value=0>>

<Message id=1076648320505745448 channel=<Thread id=1076648262217502782 name='Thread' parent=general 
owner_id=1076626012395274260 locked=False archived=False> type=<MessageType.default: 0> 
author=<Member id=881987116635160596 name='fenderbender' discriminator='5706' bot=False 
nick=None guild=<Guild id=1076626797061488640 name="fenderbender's server" shard_id=0 
chunked=False member_count=3>> flags=<MessageFlags value=0>>
"""