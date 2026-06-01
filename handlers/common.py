from aiogram import Router, types, F
from aiogram.filters.command import Command
from keyboards.keyboards import kb1


router = Router()

#Start

@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(text=f"Саламуля!\n"
                              f"Это бот с поддержкой Chat GPT\n"
                              f"Ты можешь ему задать вопрос с помощью соответствующей кнопки\n"
                              f"Любишь поиграть? Жми кнопку \"Квиз\"\n"
                              f"Не с кем поболтать? Не проблема, жми кнопку \"Разговор\"\n"
                              f"Хочешь узнать что-то новое? Бот насыпет тебе Фактов!\n"
                              f"Нужно перевести какой-то текст? Ну, кнопку ты и так видишь )", reply_markup=kb1)

@router.message(F.text == "Старт")
async def button_start(message: types.Message):
    await message.answer(text=f"Саламуля!\n"
                              f"Это бот с поддержкой Chat GPT\n"
                              f"Ты можешь ему задать вопрос с помощью соответствующей кнопки\n"
                              f"Любишь поиграть? Жми кнопку \"Квиз\"\n"
                              f"Не с кем поболтать? Не проблема, жми кнопку \"Разговор\"\n"
                              f"Хочешь узнать что-то новое? Бот насыпет тебе Фактов!\n"
                              f"Нужно перевести какой-то текст? Ну, кнопку ты и так видишь )", reply_markup=kb1)
