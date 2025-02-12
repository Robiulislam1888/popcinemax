Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from telegram import Update
... from telegram.ext import filters, CommandHandler, MessageHandler, Filters, CallbackContext
... 
... # 🔹 BotFather থেকে পাওয়া API টোকেন বসান
... BOT_TOKEN = '7333214300:AAH0f9sGxPm5ahEhl80Fbd8UXyZ-uT0l4-Y'
... 
... # 🔹 Start কমান্ডের জন্য ফাংশন
... def start(update: Update, context: CallbackContext):
...     update.message.reply_text("👋 হ্যালো! আমাকে মুভির নাম দিন, আমি ডাউনলোড লিংক পাঠাবো।")
... 
... # 🔹 মুভি নাম পাঠালে ডাউনলোড লিংক পাঠানোর ফাংশন
... def send_movie_link(update: Update, context: CallbackContext):
...     movie_name = update.message.text
...     # এখানে মুভির ডাউনলোড লিংক জেনারেট করা হচ্ছে (আপনার লিংক ব্যবহার করুন)
...     download_link = f"https://example.com/download/{movie_name.replace(' ', '_')}"
...     update.message.reply_text(f"🎬 {movie_name} ডাউনলোড করুন: {download_link}")
... 
... # 🔹 বট চালানোর জন্য ফাংশন
... def main():
...     updater = Updater(BOT_TOKEN)
...     dp = updater.dispatcher
... 
...     dp.add_handler(CommandHandler("start", start))
...     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, send_movie_link))
... 
...     updater.start_polling()
...     updater.idle()
... 
... if __name__ == '__main__':
...     main()
... 
SyntaxError: multiple statements found while compiling a single statement
