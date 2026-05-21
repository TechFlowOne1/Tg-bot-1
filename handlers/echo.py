from aiogram import Router, types, F
from aiogram.filters.command import Command
# from services.chat_gpt import ChatGptService


router = Router()

@router.message(F.text)
async def echo(message: types.Message):
    if message.text == 'стоп':
        await message.answer("Хочешь остановить работу?")
    elif "да" in message.text:
        await message.answer("Останавливаемся???!!!!")
    else:
        await message.answer(f"Ты написал {message.text}, не знаю такой команды")

# role_text = """Ты эксперт HR и помощник в телеграмм боте. Отвечай на русском языке. Если вопрос по вакансия IT, то объясняй подробно для новичков"""
        # answer = chat_gpt_service.ask(
        #     user_text=message.text,
        #     role_text=role_text,
        # )