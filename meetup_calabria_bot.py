import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv('BOT_TOKEN', '7747494089:AAGPclfh1zO_I76QBanSrTiyjW2kPi07z44')
USERNAME = "wearwearweedweear"
WHATSAPP = "+393510171397"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Telegram", url=f"https://t.me/{USERNAME}")],
        [InlineKeyboardButton("WhatsApp", url="https://wa.me/393510171397")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"Ciao! Contattami:\n\nTelegram: @{USERNAME}\nWhatsApp: {WHATSAPP}", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Telegram", url=f"https://t.me/{USERNAME}")],
        [InlineKeyboardButton("WhatsApp", url="https://wa.me/393510171397")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Contattami!", reply_markup=reply_markup)

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Bot avviato su Railway!")
    print(f"Telegram: @{USERNAME}")
    print(f"WhatsApp: {WHATSAPP}")
    
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()