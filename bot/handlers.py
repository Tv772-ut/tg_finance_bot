# bot/handlers.py

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 欢迎使用未来科技财务机器人！")

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
