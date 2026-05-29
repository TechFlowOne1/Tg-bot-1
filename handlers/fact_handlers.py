from aiogram import Router, F
from aiogram.types import Message
from services.chat_gpt import ask_gpt, user_history
from aiogram.types import FSInputFile
from keyboards.keyboards import fact_keyboard, kb1

router = Router()

@router.message(F.text == "Рандомный факт")
async def send_random_fact(message: Message):
    user_key = f"fact_{message.from_user.id}"
    if user_key not in user_history:
        user_history[user_key] = []
    await message.answer("Думаю...")

    photo = FSInputFile("assets/fact.jpg")

    prompt = """Расскажи короткий и интересный научный факт, каждый раз выбирай разные темы
    сначала 1 факт про космос, если пользователь спросил еще факт, то даёшь факт из другой области и так далее"""
    fact = await ask_gpt(user_id=user_key, user_message=prompt)

    await message.answer_photo(photo=photo)
    await message.answer(
        text=fact,
        reply_markup=fact_keyboard
    )

@router.message(F.text == "Ещё факт")
async def handle_more_fact(message: Message):
    await send_random_fact(message)

@router.message(F.text == "Закончить")
async def handle_finish(message: Message):
    user_key = f"fact_{message.from_user.id}"
    user_history[user_key] = []
    await message.answer("Оки, сворачиваемся!", reply_markup=kb1)