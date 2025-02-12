from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "7333214300:AAH0f9sGxPm5ahEhl80Fbd8UXyZ-uT0l4-Y"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! আমি মুভি ডাউনলোড বট। মুভির নাম দিন, আমি লিংক দেব।")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
