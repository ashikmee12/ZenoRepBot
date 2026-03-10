import os
import re
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# লগিং সেটআপ
logging.basicConfig(level=logging.INFO)

# ===== আপনার তথ্য =====
BOT_TOKEN = "8688557974:AAHvHzYWINrRDfGnKymO2gfUdP01J7R3IjQ"
CHANNEL_ID = -1003120043320
YOUR_WEBSITE = "www.animethic.xyz"
YOUR_CHANNEL = "@animethic2"
# ======================

def replace_content(text):
    """সব লিংক এবং মেনশন প্রতিস্থাপন করে"""
    if not text:
        return text
    try:
        # ওয়েবসাইট লিংক প্রতিস্থাপন
        text = re.sub(r'https?://[^\s]+|www\.[^\s]+', YOUR_WEBSITE, text, flags=re.IGNORECASE)
        # চ্যানেল মেনশন প্রতিস্থাপন
        text = re.sub(r'@[a-zA-Z0-9_]+', YOUR_CHANNEL, text)
    except:
        pass
    return text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('✅ বট চালু আছে! ফাইল পাঠান।')

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        original_caption = update.message.caption or ""
        new_caption = replace_content(original_caption)
        
        if update.message.document:
            await context.bot.send_document(
                chat_id=CHANNEL_ID,
                document=update.message.document.file_id,
                filename=update.message.document.file_name,
                caption=new_caption
            )
            await update.message.reply_text("✅ ডকুমেন্ট ফরোয়ার্ড করা হয়েছে!")
            
        elif update.message.video:
            await context.bot.send_video(
                chat_id=CHANNEL_ID,
                video=update.message.video.file_id,
                caption=new_caption
            )
            await update.message.reply_text("✅ ভিডিও ফরোয়ার্ড করা হয়েছে!")
            
    except Exception as e:
        await update.message.reply_text(f"❌ সমস্যা: {str(e)}")

def main():
    print("🤖 বট চালু হচ্ছে...")
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.DOCUMENT | filters.VIDEO, handle_file))
    print("✅ বট চালু হয়েছে!")
    app.run_polling()

if __name__ == "__main__":
    main()
