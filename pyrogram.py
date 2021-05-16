from pyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}")


app.run()
