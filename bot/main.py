import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start_cmd (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот-напоминалка Вахтанг. \n"
        "Напиши /help чтобы узнать, что я умею."
    )

async def help_cmd (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - начать\n"
        "/help - список команд\n"
        "/remind - (скоро) добавить напоминание"
    )

async def remind_cmd (update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я напомню об этом в \n"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("remind", remind_cmd))
    print("Бот запущен...")
    app.run_polling()
