# 📄 bot/main.py

import logging
from telegram.ext import Application, CommandHandler
from bot.handlers import register_handlers
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

def main():
    logging.basicConfig(level=logging.INFO)
    application = Application.builder().token(BOT_TOKEN).build()

    register_handlers(application)

    logging.info("🤖 未来科技财务机器人启动中...")
    application.run_polling()

if __name__ == '__main__':
    main()
