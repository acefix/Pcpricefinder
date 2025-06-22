
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import re

TOKEN = "YOUR_BOT_TOKEN"

def estimate_pc_price(text):
    patterns = {
        'i3': 100, 'i5': 150, 'i7': 200,
        '8gb': 30, '16gb': 60, '32gb': 100,
        'ssd': 50, 'hdd': 30,
        'gtx 1050': 100, 'gtx 1650': 150, 'rtx 3060': 300, 'rtx 3070': 400, 'rtx 3080': 500
    }
    price = 100  # базовая цена
    text = text.lower()
    for k, v in patterns.items():
        if k in text:
            price += v
    return price

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Отправь мне характеристики ПК, и я оценю его стоимость.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    estimated_price = estimate_pc_price(user_message)
    await update.message.reply_text(f"Примерная цена: {estimated_price} у.е.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
