import os 
from pyrogram import Client, filters
from config import Config
botid = Config.BOT_TOKEN.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	bot_get = await client.get_me()
	await message.reply_text(f"Total User:- {total_user()}\nBot :- @{bot_get.username}\nCreator :- @Snowball_Official\nLanguage :-Python3\nLibrary :- Pyrogram\nServer :- Heroku\nTotal Renamed File :-{total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} ",quote=True)
