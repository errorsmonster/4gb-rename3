from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month

	**VIP 3 **
	Daily Upload limit 250GB
	Price Rs 120 🇮🇳/🌎 1.44$  per Month

	
	**VIP 4 **
	Daily Upload limit 1000GB
	Price Rs 330 🇮🇳/🌎 3.97$  per Month
	
	Pay Using Upi I'd <code> ritesh.r8@paytm </code>
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Snowball_Official")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/Snowball_Official"),
        			InlineKeyboardButton("UPI ",url = "https://telegra.ph/file/be816cbcc38e58af3ae8a.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**VIP 1 ** 
	Daily  Upload  limit 10GB
	Price Rs 55  🇮🇳/🌎 0.67$  per Month
	
	**VIP 2 **
	Daily Upload limit 50GB
	Price Rs 80  🇮🇳/🌎 0.97$  per Month

	**VIP 3 **
	Daily Upload limit 250GB
	Price Rs 120 🇮🇳/🌎 1.44$  per Month

	
	**VIP 4 **
	Daily Upload limit 1000GB
	Price Rs 330 🇮🇳/🌎 3.97$  per Month
	
	Pay Using Upi I'd <code> ritesh.r8@paytm </code>
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Snowball_Official")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://t.me/Snowball_Official"),
        			InlineKeyboardButton("Paytm",url = "https://telegra.ph/file/be816cbcc38e58af3ae8a.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
