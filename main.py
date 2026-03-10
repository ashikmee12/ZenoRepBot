import os
import re
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# লগিং সেটআপ
logging.basicConfig(level=logging.INFO)

# ===== আপনার তথ্য =====
BOT_TOKEN = "8688557974:AAHvHzYWINrRDfGnKymO2gfUdP01J7R3IjQ"
CHANNEL_ID = -1003120043320
YOUR_WEBSITE = "www.animethic.xyz"
YOUR_CHANNEL = "@animethic2"
# ======================

def replace_content(text):
    if not text:
        return text
    # ওয়েবসাইট লিংক
    text = re.sub(r'https?://[^\s]+|www\.[^\s]+', YOUR_WEBSITE, text)
    # চ্যানেল মেনশন
    text = re.sub(r'@[a-zA-Z0-9_]+', YOUR_CHANNEL, text)
    return text

def start(update, context):
    update.message.reply_text('বট চালু আছে! ফাইল পাঠান।')

def handle_file(update, context):
    try:
        caption = update.message.caption or ""
        new_caption = replace_content(caption)
        
        if update.message.document:
            update.message.forward(CHANNEL_ID)
        elif update.message.video:
            update.message.forward(CHANNEL_ID)
            
        update.message.reply_text("✅ ফরোয়ার্ড করা হয়েছে!")
    except Exception as e:
        update.message.reply_text(f"Error: {str(e)}")

def main():
    print("বট চালু হচ্ছে...")
    updater = Updater(BOT_TOKEN)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.document | Filters.video, handle_file))
    print("বট চালু হয়েছে!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
