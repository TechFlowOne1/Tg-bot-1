from aiogram import Router, types, F
from aiogram.filters.command import Command


router = Router()

@router.message(F.text)
async def echo(message: types.Message):
    if message.text == 'стоп':
        await message.answer("Работа остановлена")
    else:
        await message.answer(f"Ты написал {message.text}, не знаю такой команды")