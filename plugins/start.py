from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Bot news 🤩", url="https://t.me/DGUuz")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/president_tuychiyev")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>❕\n♻️ Welcome to <b>@viaYTbot</b>\n\n👉🏼 <a href='https://telegra.ph/More-info-01-09'>for More info</a> 👈🏼"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
