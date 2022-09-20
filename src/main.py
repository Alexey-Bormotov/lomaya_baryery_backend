from fastapi import FastAPI
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters)

from src.api.routers import router
from src.bot.handlers import start, registration_form_init, web_app_data
from src.core.settings import settings

app = FastAPI()

app.include_router(router)


def create_bot():
    """Создать бота."""
    bot_app = ApplicationBuilder().token(settings.BOT_TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    # для тестирования команда '/reg'
    bot_app.add_handler(CommandHandler('reg', registration_form_init))
    bot_app.add_handler(
        MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))
    return bot_app


async def start_bot():
    """Запустить бота."""
    bot_app = create_bot()
    await bot_app.updater.initialize()
    await bot_app.initialize()
    await bot_app.updater.start_polling()
    await bot_app.start()
