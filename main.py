import asyncio
import logging
from aiogram import Bot, Dispatcher
import config
from handlers import common, echo, gpt_handlers, inline_handlers, fact_handlers, quiz_handlers
from handlers import inline_handlers

async def main():
    TOKEN_TG = config.token_telegram

    # Включаем логирование
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN_TG)
    dp = Dispatcher()

    # Здесь мы подрубаем роутеры в любом порядке, КРОМЕ
    # Эхо бота. Обязательно должен стоять последним, иначе будет ловить ЛЮБЫЕ сообщения в чат
    # Что нам конечно же не нужно, иначе ничего не отработает из-за перехватки эхо ботом

    dp.include_router(common.router)
    dp.include_router(gpt_handlers.router)
    dp.include_router(fact_handlers.router)
    dp.include_router(inline_handlers.router)
    dp.include_router(quiz_handlers.router)
    dp.include_router(echo.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())



