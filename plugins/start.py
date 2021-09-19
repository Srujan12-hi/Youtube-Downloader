from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("My Dev", url="https://t.me/Sruja_12")],
        [InlineKeyboardButton(
            "If any bugs", url="https://t.me/Sruja_12_pa_bot")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n I am a **Youtube Video downloader bot**\n\n Made By [Srujan](https://t.me/Sruja_12)\n\n I can Download Videos from **Youtube** Links\n Click /help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
