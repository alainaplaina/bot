#BotFather

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import pandas
import os
import random
import Beautysoulp

print("botfahter")

TOKEN = "YOUR_BOT_TOKEN"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I'm a bot. Type /help to see commands.")

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text("Available commands:\n/start - Welcome message\n/help - Show this message")

def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
