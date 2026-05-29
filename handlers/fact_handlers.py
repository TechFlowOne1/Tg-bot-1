from aiogram import Router, F
from aiogram.types import Message
from services.chat_gpt import ask_gpt, user_history
from aiogram.types import FSInputFile
from keyboards.keyboards import fact_keyboard, kb1

router = Router()

@router.message(F.text == "Рандомный факт")
async def send_random_fact(message: Message):
    user_history[f"fact_{message.from_user.id}"] = []
    await message.answer("Думаю...")

    photo = FSInputFile("assets/fact.jpg")

    prompt = "Расскажи короткий и интересный научный факт"
    fact = await ask_gpt(user_id=f"fact_{message.from_user.id}", user_message=prompt)

    await message.answer_photo(
        photo=photo,
        caption=fact,
        reply_markup=fact_keyboard
    )

@router.message(F.text == "Еще факт")
async def handle_more_fact(message: Message):
    await send_random_fact(message)

@router.message(F.text == "Закончить")
async def handle_finish(message: Message):
    user_history[f"fact{message.from_user.id}"] = []
    await message.answer("Оки, сворачиваемся!", reply_markup=kb1)