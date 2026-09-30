import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

WEB_APP_URL = "https://cqrnewinvest.com"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Ouvri CqrNewInvest",
                web_app=WebAppInfo(url=WEB_APP_URL),
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Byenveni nan CqrNewInvest!\n\n"
        "Klike sou bouton ki anba a pou ouvri aplikasyon an.",
        reply_markup=reply_markup,
    )


async def app(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Ouvri CqrNewInvest",
                web_app=WebAppInfo(url=WEB_APP_URL),
            )
        ]
    ]

    await update.message.reply_text(
        "Klike anba a pou ouvri CqrNewInvest.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 Kòmand yo:\n\n"
        "/start - Kòmanse bot la\n"
        "/app - Ouvri CqrNewInvest\n"
        "/help - Èd"
    )


def main():
    token = os.getenv("BOT_TOKEN")

    if not token:
        raise ValueError("BOT_TOKEN pa jwenn nan environment variables.")

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("app", app))
    application.add_handler(CommandHandler("help", help_command))

    print("Bot la ap kouri...")
    application.run_polling()


if __name__ == "__main__":
    main()
