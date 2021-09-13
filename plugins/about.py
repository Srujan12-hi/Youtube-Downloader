from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("My Dev", url="https://t.me/Sruja_12")],
        [InlineKeyboardButton(
            "If any bugs", url="https://t.me/Sruja_12_pa_bot")]
    ])
    welcomed = f"📕 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 ,

○ My Name : YouTube Video Downloader

○ language : Python 

○ Frame work : Pyrogran

○ Server : Heroku

○ Version : 1.0.0

○ Creator : @Sruja_12"
  
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
