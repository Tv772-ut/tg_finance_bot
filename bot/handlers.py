from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, MessageHandler, Filters
from utils.helpers import parse_amount, format_time
from models import init
from models.init import Session, Record, User

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    update.message.reply_text(
        f"👋 欢迎使用未来科技记账机器人，{user.first_name}！\n"
        "输入金额即可自动记账，例如：`20 早餐`"
    )
    session = Session()
    if not session.query(User).filter_by(user_id=user.id).first():
        session.add(User(user_id=user.id, name=user.first_name))
        session.commit()
    session.close()

def record_expense(update: Update, context: CallbackContext):
    text = update.message.text.strip()
    user = update.effective_user
    parsed = parse_amount(text)
    if not parsed:
        update.message.reply_text("❌ 无法解析金额，请输入格式如：`20 晚餐`")
        return

    amount, category = parsed
    session = Session()
    user_obj = session.query(User).filter_by(user_id=user.id).first()
    if not user_obj:
        user_obj = User(user_id=user.id, name=user.first_name)
        session.add(user_obj)
        session.commit()

    record = Record(user_id=user.id, amount=amount, category=category)
    session.add(record)
    session.commit()
    session.close()

    update.message.reply_text(f"✅ 已记账：{amount} 元，分类：{category}")

def register_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, record_expense))
