from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["about"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("My Dev", url="https://t.me/Sruja_12")],
        [InlineKeyboardButton(
            "If any bugs", url="https://t.me/Sruja_12_pa_bot")]
    ])
    welcomed = f''' 📕 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 ,

○ My Name : YouTube Video Downloader

○ language : Python 3.8.7

○ Frame work : Pyrogram

○ Server : Heroku

○ Version : 1.0.0

○ Creator : @Sruja_12 

○ Source Code :- [Click Here](https://t.me/source_code_of_file_store_bot/2)'''
  
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
