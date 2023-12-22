import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit , usertype,addpre
from config import Config


from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)


@Client.on_message(filters.private & filters.user(Config.ADMIN) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔") 


@Client.on_message(filters.private & filters.user(Config.ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("Select Plan.........",quote=True,reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("VIP 1",callback_data = "vip1"), 
        			InlineKeyboardButton("VIP 2",callback_data = "vip2") ], 
					[InlineKeyboardButton("VIP 3",callback_data = "vip3"), 
        			InlineKeyboardButton("VIP 4",callback_data = "vip4")]]))
        			

@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 10737418240
	uploadlimit(int(user_id),10737418240)
	usertype(int(user_id),"VIP1")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 10 GB")
	await bot.send_message(user_id,"Hey Ur Upgraded To VIP 1 check your plan here /myplan")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 53687091200
	uploadlimit(int(user_id),53687091200)
	usertype(int(user_id),"VIP2")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 50 GB")
	await bot.send_message(user_id,"Hey Ur Upgraded To VIP 2 check your plan here /myplan")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 268687091200
	uploadlimit(int(user_id),268687091200)
	usertype(int(user_id),"VIP3")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 250 GB")
	await bot.send_message(user_id,"Hey Ur Upgraded To VIP 3 check your plan here /myplan")

@Client.on_callback_query(filters.regex('vip4'))
async def vip4(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 1074000091200
	uploadlimit(int(user_id),1074000091200)
	usertype(int(user_id),"VIP4")
	addpre(int(user_id))
	await update.message.edit("Added successfully To Premium Upload limit 1000 GB")
	await bot.send_message(user_id,"Hey Ur Upgraded To VIP 4 check your plan here /myplan")
