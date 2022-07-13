# Parham Utilities Beta
# Credits:
# NPC
# Thanks Number1 For Helping Alot!
import time
uptimes = round(time.time())
import multiprocessing
def hosting():
  from flask import Flask
  from waitress import serve
  app = Flask("app")
  @app.route("/")
  def bot():
    return "Working...!"
  serve(app, host="0.0.0.0", port=80)
hosted = multiprocessing.Process(target = hosting)
hosted.start()
import os
import disnake
from disnake.ext import commands
import random
import sys
import requests

def clear_console(): #Credits: Doci Team
    if os.name in ["nt", "dos"]: #Check OS Name
        try: os.system("cls")
        except: pass
    else:
        try: os.system("clear")
        except: pass
    return

def change_title(title: str): #Credits: Doci Team
    if os.name in ["nt", "dos"]: #Check OS Name
        try: os.system("title "+title)
        except: pass
    return

class color: #Credits: Doci Team
    Red = "\033[91m"
    Green = "\033[92m"
    Blue = "\033[94m"
    Cyan = "\033[96m"
    White = "\033[97m"
    Yellow = "\033[93m"
    Magenta = "\033[95m"
    Grey = "\033[90m"
    Black = "\033[90m"
    Default = "\033[99m"

change_title("Parham Utilities Beta")
clear_console()

client = commands.Bot(command_prefix="!>", help_command=None, intents=disnake.Intents.all(), case_insensitive=True)
@client.event
async def on_ready():
  await client.change_presence(activity=disnake.Game(name="\"!>help\""), status=disnake.Status.dnd)
  print(color.Green+"Bot Is Working!")
@client.event
async def on_message(message): # Chat Syncing Betweeen Scratch Servers
  if not message.author.bot and not message.content == "":
    guilds = [981077071210119228, 973245403476656168]
    channels = [995718966393716817, 995721726480621618]
    if message.guild.id in guilds and message.channel.id in channels and len(str(message.author)) < 32 and len(message.content) < 1800 and not message.content.endswith("\\"):
      for channel in channels:
        channel = disnake.utils.get(client.get_all_channels(), id=channel)
        webhook = disnake.utils.get(await channel.webhooks(), name="Parham Utilities Beta")
        if webhook is None:
          webhook = await channel.create_webhook(name="Parham Utilities Beta")
        await webhook.send(message.content+"\n\n*Server:* `"+message.guild.name+"`\n*Channel:* <#"+str(message.channel.id)+">", username=str(message.author), avatar_url=message.author.avatar, files=[await file.to_file() for file in message.attachments], allowed_mentions= disnake.AllowedMentions(users=False, roles=False, everyone=False, replied_user=False))
    await client.process_commands(message)
  return
@client.event 
async def on_command_error(ctx, error): 
  if isinstance(error, commands.CommandNotFound): await ctx.send("Error ❌", embed=disnake.Embed(title="Error ❌", description="Error:\nCommand Not Found", color=0xFF0000))
@client.command()
async def help(ctx):
  await ctx.send(embed=disnake.Embed(title="Help", description="`!>credits` *See Our Developers*\n`!>chatbot {message}` *Chat With Bot*\n`!>uptime` Bot Up Time\n`/sudo {member} {message}` *Copy Someone*\n**More Soon...**", color=0x3EC70B))
@client.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓 My Ping Is `"+str(round(client.latency*1000))+"`")
@client.command()
async def exit(ctx):
  if ctx.author.id == 740442702851604510:
    await ctx.send(embed=disnake.Embed(title="Exit", description="Exiting...", color=0xFF0000))
    await client.close()
    global hosted
    hosted.terminate()
    sys.exit(3)
@client.command()
async def credits(ctx):
  await ctx.send(embed=disnake.Embed(title="Credits", description="Made By Parham\nCredits:\n> NPC\nThanks Number1 For Helping Alot!", color=random.randint(0, 16777215)))
@client.command()
async def uptime(ctx):
  global uptimes
  await ctx.send(embed=disnake.Embed(title="Up Time", description=f"Up Time: <t:{uptimes}:R>", color=0x66FFFF))
@client.command()
async def chatbot(ctx, *, arg):
  try: 
    msg = arg.replace(" ", "+")
    chat = requests.get(f"https://api.popcat.xyz/chatbot?msg={msg}&owner=Parham&botname=Parham+Utilities+Beta").json()["response"]
    await ctx.send(embed=disnake.Embed(title="Chat", description="```\n"+chat+"\n```", color=random.randint(0, 16777215)))
  except: 
    await ctx.send(embed=disnake.Embed(title="Something Goes Wrong", description="Try Again Later...", color=0xFF0000))
@client.slash_command(dm_permission=False)
async def sudo(inter, member: disnake.Member, message: str):
  """
  Copy Someone

  Parameters
  ----------
  member: Who To Copy
  message: Message To Be Said
  """
  try:
    webhook = disnake.utils.get(await inter.channel.webhooks(), name="Parham Utilities Beta")
    if webhook is None: webhook = await inter.channel.create_webhook(name="Parham Utilities Beta")
    await webhook.send(message[0:2000], avatar_url=member.avatar, username=member.display_name, allowed_mentions= disnake.AllowedMentions(users=True, roles=False, everyone=False, replied_user=False))
    await inter.send("Successfully ✔️", embed=disnake.Embed(title="Successfully ✔️", description="Successfully Sent Message As `"+member.display_name+"`", color=random.randint(0, 16777215)), ephemeral=True)
  except Exception as error: await inter.send("Error ❌", embed=disnake.Embed(title="Error ❌", description="Error:\n```\n"+str(error)+"\n```", color=0xFF0000), ephemeral=True)
@client.slash_command()
async def evalpy(inter, command: str, ephemeral: bool = True):
  """
  Eval (Owner Only)

  Parameters
  ----------
  command: Code To Run
  ephermeral: Ephermeral?
  """
  if inter.author.id == 740442702851604510:
    try:
      output = eval(command)
      await inter.send("Eval Complete!", embed=disnake.Embed(title="Eval Complete!", description="Eval Complete! Output:\n```\n"+str(output)+"\n```", color=random.randint(0, 16777215)), ephemeral=ephemeral)
    except Exception as error: await inter.send("Error ❌", embed=disnake.Embed(title="Error ❌", description="Error:\n```\n"+str(error)+"\n```", color=0xFF0000), ephemeral=ephemeral)
  else: await inter.send("Error ❌", embed=disnake.Embed(title="Error ❌", description="Error:\nYou Don't Own This Bot", color=0xFF0000), ephemeral=True)
client.run(os.environ["Token"])
sys.exit(2)