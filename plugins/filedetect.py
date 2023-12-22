from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, InlineKeyboardMarkup, ForceReply)

from pyrogram.enums import MessageMediaType

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message
    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
        new_name = message.text
        await message.delete()
        msg = await client.get_messages(message.chat.id, reply_message.id)
        file = msg.reply_to_message
        media = getattr(file, file.media.value)
        if not "." in new_name:
            if "." in media.file_name:
                extn = media.file_name.rsplit('.', 1)[-1]
            else:
                extn = "mkv"
            new_name = new_name + "." + extn
        await reply_message.delete()

        button = [[InlineKeyboardButton(
            "📁 Dᴏᴄᴜᴍᴇɴᴛ", callback_data="doc")]]
        if file.media in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
            button.append([InlineKeyboardButton(
                "🎥 Vɪᴅᴇᴏ", callback_data="vid")])
        elif file.media == MessageMediaType.AUDIO:
            button.append([InlineKeyboardButton(
                "🎵 Aᴜᴅɪᴏ", callback_data="aud")])
        
        await message.reply(
            text=f"**Sᴇʟᴇᴄᴛ Tʜᴇ Oᴜᴛᴩᴜᴛ Fɪʟᴇ Tyᴩᴇ**\n**• Fɪʟᴇ Nᴀᴍᴇ :-** <code>{new_name}</code>",
            reply_to_message_id=file.id,
            reply_markup=InlineKeyboardMarkup(button)
        )