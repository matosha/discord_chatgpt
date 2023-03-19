import discord, os,json #python3 -m pip install python-dotenv discord.py
import requests
from dotenv import load_dotenv 

load_dotenv()

intents = discord.Intents.all()  # enable all intents
client = discord.Client(intents=intents)  # create the client

def image_get(message):
  myobj = {"prompt": message, "n": 1, "size": "1024x1024"  }
  return json.loads((requests.post("https://api.openai.com/v1/images/generations", json = myobj,headers={"Content-Type":"application/json", "Authorization":"Bearer "+os.getenv('OPENAI_API_KEY')})).text)["data"][0]["url"]

@client.event
async def on_message(message):
 token=os.getenv('OPENAI_API_KEY')
 if message.content.startswith(f"<@{client.user.id}> help"):
  await message.channel.send("@<gptUser> <ask any question you want>\r\n @<gptUser> image <ask for an image you want>")

 elif message.content.startswith(f"<@{client.user.id}> image"):
  text = message.content.replace(f"<@{client.user.id}> image", "")
  print("Asked:"+text)
  respon=image_get(text)
  if "ability to provide images" not in respon:
   await message.channel.send(image_get(text))

 elif message.content.startswith(f"<@{client.user.id}>"):
  text = message.content.replace(f"<@{client.user.id}>", "")
  print("Asked:"+text)
  myobj = {"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": text}],"temperature": 0.7}
  req=requests.post("https://api.openai.com/v1/chat/completions", json = myobj, headers={"Content-Type":"application/json", "Authorization":"Bearer "+token})
  json_l=json.loads(req.text)["choices"][0]["message"]["content"]
  await message.channel.send(json_l)  # send the response from the chatbot
 else:
  message.channel.send("@<gptUser> help")
# run the client
client.run(os.getenv('DISCORD_BOT_TOKEN'))
