from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from services.chat_gpt import ask_gpt
from aiogram.types import FSInputFile
from keyboards.keyboards import gpt_exit_keyboard, kb1


router = Router()


class GPTStates(StatesGroup):
    wait_for_question = State()

@router.message(F.text == "Задать вопрос GPT")
async def ask_gpt_start(message: types.Message, state: FSMContext):
    photo_file = FSInputFile("assets/logo_chat.jpg")
    await message.answer_photo(
        photo=photo_file,
        caption="🤖 **Ты перешел в режим ChatGPT!**\n\nВведи свой вопрос для чатика:",
        reply_markup = gpt_exit_keyboard
    )
    await state.set_state(GPTStates.wait_for_question)

@router.message(GPTStates.wait_for_question, F.text == "Выйти из режима GPT")
async def exit_gpt_mode(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Вы вышли из режима GPT", reply_markup=kb1)


@router.message(GPTStates.wait_for_question, F.text)
async def gpt_answer(message: types.Message, state: FSMContext):
    await message.answer("Думаю...")
    reply = await ask_gpt(user_message=message.text)
    await message.answer(reply)