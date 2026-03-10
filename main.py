import os
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# ===== আপনার তথ্য =====
BOT_TOKEN = "8688557974:AAHvHzYWINrRDfGnKymO2gfUdP01J7R3IjQ"
CHANNEL_ID = -1003120043320
YOUR_WEBSITE = "www.animethic.xyz"
YOUR_CHANNEL = "@animethic2"
# ======================

def replace_content(text):
    if not text:
        return text
    website_pattern = r'https?://[^\s]+|www\.[^\s]+|[a-zA-Z0-9.-]+\.(?:com|org|net|xyz)(?:/[^\s]*)?'
    website_links = re.findall(website_pattern, text, re.IGNORECASE)
    for link in website_links:
        text = text.replace(link, YOUR_WEBSITE, 1)
    channel_pattern = r'@[a-zA-Z0-9_]+'
    channels = re.findall(channel_pattern, text)
    for channel in channels:
        text = text.replace(channel, YOUR_CHANNEL, 1)
    return text

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔁 বট চালু আছে! ফাইল পাঠান, আমি লিংক পরিবর্তন করে চ্যানেলে ফরোয়ার্ড করব।"
    )

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        original_caption = update.message.caption or ""
        new_caption = replace_content(original_caption)
        
        if update.message.document:
            file = update.message.document
            await context.bot.send_document(
                chat_id=CHANNEL_ID,
                document=file.file_id,
                filename=file.file_name,
                caption=new_caption
            )
        elif update.message.video:
            video = update.message.video
            await context.bot.send_video(
                chat_id=CHANNEL_ID,
                video=video.file_id,
                caption=new_caption
            )
        
        await update.message.reply_text("✅ চ্যানেলে পাঠানো হয়েছে!")
        
    except Exception as e:
        await update.message.reply_text(f"❌ সমস্যা: {str(e)}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VIDEO | filters.DOCUMENT, handle_file))
    print("বট চালু...")
    app.run_polling()

if __name__ == "__main__":
    main()
