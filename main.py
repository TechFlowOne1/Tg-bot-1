import asyncio
import logging
from aiogram import Bot, Dispatcher
import config
from handlers import common, echo, career_choice, inline_handlers
# from services.chat_gpt import ChatGptService


async def main():
    TOKEN_TG = config.token_telegram
    # TOKEN_OPENAI = config.token_openai

    # Включаем логирование
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN_TG)
    dp = Dispatcher()

    # chat_gpt_service = ChatGptService(api_key=TOKEN_OPENAI)
    # dp["chat_gpt_service"] = chat_gpt_service

    dp.include_router(common.router)
    dp.include_router(career_choice.router)
    dp.include_router(inline_handlers.router)
    dp.include_router(echo.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


