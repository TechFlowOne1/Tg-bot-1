from aiogram import Router, types, F
from aiogram.filters.command import Command
from keyboards.keyboards import kb1


router = Router()

#Start

@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f"Привет!, {message.chat.first_name}!", reply_markup=kb1)

@router.message(F.text == "Старт")
async def button_start(message: types.Message):
    await message.answer(f"Привет, {message.chat.first_name}!", reply_markup=kb1)

#Info

@router.message(Command("info"))
async def command_info(message: types.Message):
    await message.answer("Это бот с подключением Chat GPT. Ты можешь воспользоваться моими функциями используя кнопки!", reply_markup=kb1)

@router.message(F.text == "Инфо")
async def button_info(message: types.Message):
    await message.answer("Это бот с подключением Chat GPT. Ты можешь воспользоваться моими функциями используя кнопки!", reply_markup=kb1)

