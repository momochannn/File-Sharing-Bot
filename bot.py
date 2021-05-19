import pyromod.listen
from pyrogram import Client
import sys

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                self.invitelink = link
            except:
                self.LOGGER(__name__).warning("Bot tidak bisa mengekspor link undangan dari Force Sub Channel!")
                self.LOGGER(__name__).warning("Harap periksa kembali nilai FORCE_SUB_CHANNEL dan Pastikan Bot adalah Admin di saluran dengan Undang Pengguna melalui Izin Tautan")
                self.LOGGER(__name__).info("\nBot Dihentikan. Harap hubungi https://t.me/kenkanasw untuk mendapatkan dukungan")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning("Pastikan bot adalah Admin di Channel DB, dan periksa kembali Nilai CHANNEL_ID Value")
            self.LOGGER(__name__).info("\n💢MAAF BOT ERROR💢 Owner https://t.me/kenkanasw")
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(f"💠BOT SUDAH SIAP DIGUNAKAN💠\n\nCreated by 𝘾𝙤𝙙𝙚 𝕏 𝘽𝙤𝙩𝙯\nhttps://t.me/kenkanasw")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("💢BOT ERROR💢")
