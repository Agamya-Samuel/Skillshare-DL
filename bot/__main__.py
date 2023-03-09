from bot.main_node import download_node

from bot import (DL_LINKS_MASTER_MONGODB_URL, DL_LINKS_MASTER_MONGODB_DATABASE_NAME, DL_LINKS_MASTER_MONGODB_COLLECTION_NAME)

import os

from telegram.ext import CommandHandler
from telegram.ext import Updater, MessageHandler, Filters

import logging

from telegram import Update
from telegram.ext import CallbackContext

from bot import (BOT_TOKEN)

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


# Callback functions
def start_callback(update, context):
    user_msg = context.args
    update.message.reply_text('Welcome to Skillshare DL Bot. Using this bot you can download Skillshare courses for Free !!!. Just send me any Skillshare course Link.')

def dl_callback(update, context):
    user_msg = context.args
    update.message.reply_text('Your Course is Downloading...')
    skillshr_link = str(update.message.text)
    user_id = update.effective_chat.id
    print(f'{user_id = }')

    # Replying back Download Links
    urls = download_node(course_url = skillshr_link, from_user_id = user_id)
    msg = f'Anonfile Url = {urls[0]}\n'
    msg += f'Pixeldrain Url = {urls[1]}'
    update.message.reply_text(msg)
    
def dl_echo(update: Update, context: CallbackContext):
    user_msg = update.message.reply_text('Your Course is Downloading...')
    skillshr_link = str(update.message.text)
    user_id = update.effective_chat.id
    print(f'{user_id = }')
    
    # Replying back Download Links
    urls = download_node(course_url = skillshr_link, from_user_id = user_id)
    msg = f'Anonfile Url = {urls[0]}\n'
    msg += f'Pixeldrain Url = {urls[1]}'
    update.message.reply_text(msg)


# Handlers
start_handler = CommandHandler('start', start_callback)
dl_handler = CommandHandler('dl', dl_callback)
dl_echo_handler = MessageHandler(Filters.text, dl_echo)


# adding Handlers to Dispatchers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(dl_handler)
dispatcher.add_handler(dl_echo_handler)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater.start_polling(drop_pending_updates=False)