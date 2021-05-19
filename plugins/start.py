
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait

from bot import Bot
from config import ADMINS, START_MSG, OWNER_ID
from helper_func import subscribed, encode, decode, get_messages

@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("Harap tunggu ...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Ada yang tidak beres ..!")
            return
        await temp_msg.delete()
        for msg in messages:
            try:
                await msg.copy(chat_id=message.from_user.id, reply_markup = None)
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(chat_id=message.from_user.id, reply_markup = None)
            except:
                pass
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("❌ TUTUP", callback_data = "close"),
                    InlineKeyboardButton("CHANNEL 💌", url = client.username)
                ]
            ]
        )
        await message.reply_text(
            text = START_MSG.format(firstname = message.chat.first_name),
            reply_markup = reply_markup,
            disable_web_page_preview = True,
            quote = True
        )
        return

@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    text = "<b>Anda harus join channel/Group untuk menggunakan saya\n\nTolong bergabunglah ke Channel</b>"
    message_text = message.text
    try:
        command, argument = message_text.split()
        text = text + f" <b>and <a href='https://t.me/{client.username}?start={argument}'>COBA KLIK LINK LAGI</a></b>"
    except ValueError:
        pass
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("CHANNEL 💌", url = client.invitelink)]])
    await message.reply(
        text = text,
        reply_markup = reply_markup,
        quote = True,
        disable_web_page_preview = True
    )
