import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2
from config import Config


bot = Client(

           "SnowPremiumBot",

           bot_token=Config.BOT_TOKEN,

           api_id=Config.API_ID,

           api_hash=Config.API_HASH,

           plugins=dict(root='plugins'))
           

if Config.STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
