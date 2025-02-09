import telebot
from pyarchivebox import PyArchiveBox
import config

BOT_TOKEN = config.telegram_token
bot = telebot.TeleBot(BOT_TOKEN)

archivebox = PyArchiveBox(config.archivebox_username, config.archivebox_password, config.archivebox_url)
archivebox.login()

whitelist = config.whitelist
def is_allowed(userid):
    return userid in whitelist

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if is_allowed(message.from_user.id):
        bot.reply_to(message, "You are allowed to use this bot.")
    else:
        bot.reply_to(message, "You are not allowed to use this bot, all your commands will not execute.")


@bot.message_handler(commands=["add"])
def add_url(message):
    if not is_allowed(message.from_user.id):
        bot.reply_to(message, "You are not allowed to use this bot.")
        return
    
    command_parts = message.text.split(maxsplit=1)
    if len(command_parts) < 2:
        bot.reply_to(message, "Usage: /add <url> [tags] [depth].")
        return
    
    args = command_parts[1].split(maxsplit=2)
    url = args[0]
    tags = args[1] if len(args) > 1 else None
    depth = int(args[2]) if len(args) > 2 else None

    if tags == "depth=1":
        depth = 1
        tags = None
    elif tags == "depth=0":
        depth = 0
        tags = None

    bot.send_message(message.chat.id, "Archiving started...")
    if tags and depth:
        archivebox.add(url, tags, depth=depth)
    elif tags:
        archivebox.add(url, tags)
    else:
        archivebox.add(url)

    latest = archivebox.get_latest()
    last = latest.get(0)

    response = f"Archived url: {url}\nArchive title: {last['title']}\nArchive date added: {last['date_added']}\nArchive tags: {tags}\nArchive depth: {depth}"

    bot.reply_to(message, response)


bot.infinity_polling()