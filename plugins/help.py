from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"You need help ???\n\n Ok! Send me a thumbnail (if you want a video with thumbnail)\n Send a YouTube link (Warning:- Don't send adult links)\n\n Wait till the bot process the link\n\n After that click on any quality you need\n\n And Done!!!!!\n\n The bot sends you the file/video within a short time (it depends on file size)"
    await message.reply_text(helptxt)
