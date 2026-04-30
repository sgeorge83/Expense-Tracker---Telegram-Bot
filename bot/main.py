from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from services.parser import parse_text_expense
from utils.config import settings


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome! Send expense like 'Lunch 35'.")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Commands: /start /summary /setbudget /export /help")


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text or ""
    parsed = parse_text_expense(text)
    if not parsed:
        await update.message.reply_text("Couldn't parse. Try: Fuel 120")
        return
    await update.message.reply_text(
        f"✅ Added\n\nCategory: {parsed.category}\nAmount: {parsed.amount:.2f} {parsed.currency}"
    )


def build_app() -> Application:
    app = Application.builder().token(settings.telegram_bot_token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    return app


if __name__ == "__main__":
    bot_app = build_app()
    bot_app.run_polling()
