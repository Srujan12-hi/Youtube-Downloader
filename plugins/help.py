from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"**You need help ???**\n\n Ok! Send a YouTube link (Warning:- Don't send **adult** links)\n\n Wait till the bot process the link\n\n After that click on any quality you need\n\n And Done!!!!!\n\n The bot sends you the file/video within a short time (it depends on file size)\n If you want short video files you should erase 'feature=share' and send the link.\n\nIf you are sharing link of YouTube Shorts make sure that you erase 'feature=share' in the link\nBecause bot is not update to latest version of YouTube API"
    await message.reply_text(helptxt)
