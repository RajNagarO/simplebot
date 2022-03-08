#bot.py
# from discord.ext import commands
import os
import discord 
from dotenv import load_dotenv
import json
import random
import requests


load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [  "Cheer up!",  "Hang in there.",  "You are a great person"]
question=["?","do you know","what","wt","really"]
answer=["okay okay","okay","Not Practical"]
emotions=["happy","sad","disgust","fear","anger","surprise"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('$hi' or 'hi' or 'hello' or 'ola'):
        await message.channel.send('Hello there mate!')
    if msg.startswith('$inspire'):
        quote = get_quote()
    if msg.startswith(''):
    
        await message.channel.send(quote)
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
    if any(word in msg for word in question):
        await message.channel.send(random.coice())
    if any(word in msg for word in emotions):
        await message.channel.send(random.coice())

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return (quote)



@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome to NashhRunner Discord server!'
    )


client.run(TOKEN)







# import json
# import random
# import os
# import discord 
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('TOKEN')

# client = discord.Client()

# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')

# client.run(TOKEN)

# client = discord.Client()




# @client.event



# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startwith('$inspire'):
#         quote = get_quote()
#         await message.channel.send(quote)


# token = os.getenv("TOKEN")
# client.run(token)


