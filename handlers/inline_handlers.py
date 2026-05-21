from aiogram import Router, types, F

router = Router()

@router.callback_query(F.data == "ask_gpt")
async def callback_ask_gpt(callback: types.CallbackQuery):
    await callback.message.answer("Ты нажал кнопку GPT")

@router.callback_query(F.data == "ask_yandex")
async def callback_ask_gpt(callback: types.CallbackQuery):
    await callback.message.answer("Ты нажал кнопку Yandex")

