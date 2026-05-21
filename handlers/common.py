from aiogram import Router, types, F
from aiogram.filters.command import Command
from keyboards.keyboards import kb1
from keyboards.inline_keyboard import inline_keyboard
from utils.random_fox import fox


router = Router()

#Start

@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer(f"Саламуля, {message.chat.first_name}!", reply_markup=kb1)

@router.message(F.text == "Старт")
async def button_start(message: types.Message):
    await message.answer(f"Саламуля, {message.chat.first_name}!", reply_markup=kb1)

#Info

@router.message(Command("info"))
async def command_info(message: types.Message):
    await message.answer("Это бот с подключением Chat GPT. Если хочешь остановить работу напиши 'стоп'.", reply_markup=kb1)

@router.message(F.text == "Инфо")
async def button_info(message: types.Message):
    await message.answer("Это бот с подключением Chat GPT. Если хочешь остановить работу напиши 'стоп'.", reply_markup=kb1)

#Fox

@router.message(Command("fox"))
async def command_fox(message: types.Message):
    image_fox = fox()
    await message.answer_photo(image_fox)

@router.message(F.text == "Лиса")
async def button_fox(message: types.Message):
    image_fox = fox()
    await message.answer_photo(image_fox)

