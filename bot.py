from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("🚗 Welcome to ShRish Travels!\nType /book to book a ride.")

def book(update, context):
    update.message.reply_text(
        "👉 Book your ride here:",
        reply_markup={
            "inline_keyboard": [[{
                "text": "Open Web App",
                "web_app": { "url": "https://shrishtravels.netlify.app/" }
            }]]
        }
    )

updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("book", book))

updater.start_polling()
updater.idle()
