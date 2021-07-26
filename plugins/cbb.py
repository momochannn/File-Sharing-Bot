

from pyrogram import __version__
from bot import Bot
from config import FORCE_SUB_CHANNEL
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            rpk = f"[" + user_name + "](tg://user?id=" + {FORCE_SUB_CHANNEL} + ")"
            text = f"**○ CHANNEL :** {rpk} \n○ **Language :** `Python3`\n○ **Library :** [Pyrogram asyncio {__version__}](https://docs.pyrogram.org/)",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("❌ TUTUP", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
