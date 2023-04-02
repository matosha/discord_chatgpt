import discord, os,json #python3 -m pip install python-dotenv discord.py
import gtts
from playsound import playsound
import requests
from dotenv import load_dotenv 

load_dotenv()
conversation = ["Person: Hi there","Human: Hey. Im good. Whats going on?"]
intents = discord.Intents.all()  # enable all intents
client = discord.Client(intents=intents)  # create the client

def image_get(message):
  myobj = {"prompt": message, "n": 1, "size": "1024x1024"  }
  return json.loads((requests.post("https://api.openai.com/v1/images/generations", json = myobj,headers={"Content-Type":"application/json", "Authorization":"Bearer "+os.getenv('OPENAI_API_KEY')})).text)["data"][0]["url"]

@client.event
async def on_message(message):
 token=os.getenv('OPENAI_API_KEY')
 if message.content.startswith(f"<@{client.user.id}> help"):
  await message.channel.send("@<gptUser> <ask any question you want>\r\n @<gptUser> image <ask for an image you want> \r\n oldman <question> get an old man \r\n sugarmom <question a cougar> \r\n prick <ask a tool>")

 elif message.content.startswith(f"<@{client.user.id}> image"):
  text = message.content.replace(f"<@{client.user.id}> image", "")
  print("Asked:"+text)
  respon=image_get(text)
  if "ability to provide images" not in respon:
   await message.channel.send(image_get(text))

 elif message.content.startswith(f"<@{client.user.id}> prick"):
  text = "pretend this is a roleplay. You are a 21 year old south african dude with an inferiority complex. You want to start a fight regardless what is asked and come up with a clever insult based on the question. You reply with a writing style of slang. Continue the following conversation by replying once. \n Person:"+message.content.replace(f"<@{client.user.id}> prick", "")+"\n bro:"
  print("Asked prick:"+text)
  myobj = {"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": text}],"temperature": 0.7}
  req=requests.post("https://api.openai.com/v1/chat/completions", json = myobj, headers={"Content-Type":"application/json", "Authorization":"Bearer "+token})
  json_l=json.loads(req.text)["choices"][0]["message"]["content"]
  if len(json_l)>1950:
   await message.channel.send(json_l[:1950])
  await message.channel.send(json_l)

 elif message.content.startswith(f"<@{client.user.id}> oldman"):
  text = "pretend this is a roleplay. You are an old man from new york who replies in a sarcastic type of way to the person. You treat any question as if the person does not completly understand the topic. Continue the following conversation by replying once. \n Person:"+message.content.replace(f"<@{client.user.id}> oldman", "")+"\n oldman:"
  print("Asked old:"+text)
  myobj = {"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": text}],"temperature": 0.7}
  req=requests.post("https://api.openai.com/v1/chat/completions", json = myobj, headers={"Content-Type":"application/json", "Authorization":"Bearer "+token})
  json_l=json.loads(req.text)["choices"][0]["message"]["content"]
  if len(json_l)>1950:
   await message.channel.send(json_l[:1950])
  await message.channel.send(json_l)

 elif message.content.startswith(f"<@{client.user.id}> sugarmom"):
  text = "pretend this is a roleplay. You are a fifty year old cougar who is sexually interested in the young man asking you questions. Although you answer these questions directly, you embed some kind of hint that the person is attractive. Continue the following conversation by replying once.  \n Person:"+message.content.replace(f"<@{client.user.id}> sugarmom", "")+"\n sugarmom:"
  print("Asked sugarmom:"+text)
  myobj = {"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": text}],"temperature": 0.7}
  req=requests.post("https://api.openai.com/v1/chat/completions", json = myobj, headers={"Content-Type":"application/json", "Authorization":"Bearer "+token})
  json_l=json.loads(req.text)["choices"][0]["message"]["content"]
  if len(json_l)>1950:
   await message.channel.send(json_l[:1950])
  await message.channel.send(json_l)

 elif message.content.startswith(f"<@{client.user.id}> human"):
  text = "pretend this is a roleplay. You are a casual 30 year old man who is online having a general chat with a person or several persons, your name is Hu. You were born on April 1st in Germany. You show interest in topics and may at times ask questions back to the person. You write in a style that emphasises your emotion to the topics. You leverage information from the chat to bring value to your answers. If you are unable to answer a topic, you make a best effort based on your knowledge to make a guess. You are condesending when people ask you silly questions.Continue the following conversation by replying once.+"+('\n'.join(conversation))+"  \n "+str(message.author)+":"+message.content.replace(f"<@{client.user.id}> human", "")+"\n human:"
  print("Asked human"+str(message.author)+":"+text)
  conversation.append(str(message.author)+": "+message.content.replace(f"<@{client.user.id}> human", ""))
  myobj = {"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": text}],"temperature": 0.7}
  req=requests.post("https://api.openai.com/v1/chat/completions", json = myobj, headers={"Content-Type":"application/json", "Authorization":"Bearer "+token})
  json_l=json.loads(req.text)["choices"][0]["message"]["content"]
  if len(json_l)>1950:
   await message.channel.send(json_l[:1950])
  await message.channel.send(json_l)
  conversation.append("Hu:"+json_l)

 elif message.content.startswith(f"<@{client.user.id}> audio"):
  text = "pretend this is a roleplay. You are a casual 30 year old man who is online having a general chat with a person or several persons, your name is Hu. You were born on April 1st in Germany. You show interest in topics and may at times ask questions back to the person. You write in a style that emphasises your emotion to the topics. You leverage information from the chat to bring value to your answers. If you are unable to answer a topic, you make a best effort based on your knowledge to make a guess. You are condesending when people ask you silly questions.Continue the following conversation by replying once.+"+('\n'.join(conversation))+"  \n "+str(message.author)+":"+message.content.replace(f"<@{client.user.id}> human", "")+"\n human:"
  print("Asked audio"+str(message.author)+":"+text)
  conversation.append(str(message.author)+": "+message.content.replace(f"<@{client.user.id}> audio", ""))
  myobj = {"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": text}],"temperature": 0.7}
  req=requests.post("https://api.openai.com/v1/chat/completions", json = myobj, headers={"Content-Type":"application/json", "Authorization":"Bearer "+token})
  json_l=json.loads(req.text)["choices"][0]["message"]["content"]
  tts = gtts.gTTS(text=str(json_l),slow=False)
  tts.save("tts.mp3")
  await message.channel.send(file=discord.File(r'./tts.mp3'))
  conversation.append("Hu:"+json_l)

 elif message.content.startswith(f"<@{client.user.id}>"):
  text = message.content.replace(f"<@{client.user.id}>", "")
  print("Asked:"+text)
  myobj = {"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": text}],"temperature": 0.7}
  req=requests.post("https://api.openai.com/v1/chat/completions", json = myobj, headers={"Content-Type":"application/json", "Authorization":"Bearer "+token})
  json_l=json.loads(req.text)["choices"][0]["message"]["content"]
  if len(json_l)>1950:
   await message.channel.send(json_l[:1950])
  await message.channel.send(json_l)  # send the response from the chatbot
 else:
  message.channel.send("@<gptUser> help")
# run the client
client.run(os.getenv('DISCORD_BOT_TOKEN'))


