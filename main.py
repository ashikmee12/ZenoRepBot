import os
import re
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# লগিং সেটআপ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# ===== আপনার তথ্য =====
BOT_TOKEN = "8688557974:AAHvHzYWINrRDfGnKymO2gfUdP01J7R3IjQ"
CHANNEL_ID = -1003120043320
YOUR_WEBSITE = "www.animethic.xyz"
YOUR_CHANNEL = "@animethic2"
# ======================

def replace_content(text):
    if not text:
        return text
    try:
        # ওয়েবসাইট লিংক খুঁজে বের করা
        website_pattern = r'https?://[^\s]+|www\.[^\s]+'
        website_links = re.findall(website_pattern, text, re.IGNORECASE)
        for link in website_links:
            text = text.replace(link, YOUR_WEBSITE, 1)
        
        # চ্যানেল মেনশন খুঁজে বের করা
        channel_pattern = r'@[a-zA-Z0-9_]+'
        channels = re.findall(channel_pattern, text)
        for channel in channels:
            text = text.replace(channel, YOUR_CHANNEL, 1)
    except:
        pass
    return text

def start(update: Update, context: CallbackContext):
    update.message.reply_text('🔁 বট চালু আছে! ফাইল পাঠান।')

def handle_file(update: Update, context: CallbackContext):
    try:
        original_caption = update.message.caption or ""
        new_caption = replace_content(original_caption)
        
        if update.message.document:
            file = update.message.document
            context.bot.send_document(
                chat_id=CHANNEL_ID,
                document=file.file_id,
                filename=file.file_name,
                caption=new_caption
            )
        elif update.message.video:
            video = update.message.video
            context.bot.send_video(
                chat_id=CHANNEL_ID,
                video=video.file_id,
                caption=new_caption
            )
        
        update.message.reply_text("✅ চ্যানেলে পাঠানো হয়েছে!")
        
    except Exception as e:
        update.message.reply_text(f"❌ সমস্যা: {str(e)}")

def main():
    print("বট চালু হচ্ছে...")
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document | Filters.video, handle_file))
    
    print("বট চালু হয়েছে!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
