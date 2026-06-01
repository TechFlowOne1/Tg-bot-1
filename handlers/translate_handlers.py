from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
# Импортируем инструменты для создания состояний
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.translate_keyboards import lang_keyboard, translate_control_keyboard
from keyboards.keyboards import kb1
from services.chat_gpt import ask_gpt, user_history
from aiogram.filters import Command

translate_router = Router()

# Создаем состояния для переводчика

class TranslateStates(StatesGroup):
    wait_for_lang = State()     # Ждем, пока юзер тыкнет на язык
    wait_for_text = State()     # Ждем текст для перевода


# Нажатие на кнопку "Переводчик" в главном меню

@translate_router.message(F.text == "Переводчик")
async def start_translate_mode(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(TranslateStates.wait_for_lang)
    await message.answer(
        text="Выбери язык, на который нужно перевести текст:",
        reply_markup=lang_keyboard
    )


# Обработка выбора языка с инлайн кнопок

@translate_router.callback_query(TranslateStates.wait_for_lang, F.data.startswith("lang_"))
async def choose_language(callback: CallbackQuery, state: FSMContext):
    languages = {
        "lang_en": "Английский",
        "lang_es": "Испанский",
        "lang_de": "Немецкий",
        "lang_fr": "Французский"
    }

    chosen_lang = languages[callback.data]
    await state.update_data(target_lang=chosen_lang)  # Запоминаем язык в память состояний
    await state.set_state(TranslateStates.wait_for_text)  # Переключаем на шаг ожидания текста

    await callback.answer()

    # Прячем нижние кнопки

    await callback.message.answer(
        text=f"Выбран язык: {chosen_lang}.\nОтправь мне текст, который нужно перевести: 👇",
        reply_markup=ReplyKeyboardRemove()
    )


# Прием текста от юзера и отправка в Chat GPT

@translate_router.message(TranslateStates.wait_for_text, F.text)
async def handle_translation(message: Message, state: FSMContext):
    data = await state.get_data()
    target_lang = data.get("target_lang", "Английский")

    await message.answer("Перевожу... ⏳")

    # Формируем четкую инструкцию для GPT

    prompt = (
        f"Ты профессиональный переводчик. Переведи следующий текст строго на {target_lang} язык. "
        f"Выведи ТОЛЬКО готовый перевод, без лишних фраз, твоих комментариев и кавычек.\n\nТекст:\n{message.text}"
    )

    # Используем уникальный временный ключ чтобы перевод не ломал обычную историю общения с GPT
    temp_key = f"trans_{message.from_user.id}"
    translation = await ask_gpt(user_id=temp_key, user_message=prompt)

    # Сразу чистим за собой историю этого временного ключа
    if temp_key in user_history:
        user_history[temp_key] = []
    await message.answer(text=translation, reply_markup=translate_control_keyboard)


# Инлайн кнопка "Сменить язык"

@translate_router.callback_query(F.data == "translate_change")
async def change_lang_callback(callback: CallbackQuery, state: FSMContext):
    await state.set_state(TranslateStates.wait_for_lang)
    await callback.answer()
    await callback.message.answer(text="Выбери новый язык:", reply_markup=lang_keyboard)


# Инлайн кнопка "Закончить" (сбрасывает состояния FSM и отправляет стартовое меню)
@translate_router.callback_query(F.data == "translate_finish")
async def finish_translate_callback(callback: CallbackQuery, state: FSMContext):
    await state.clear()  # Полностью сбрасываем шаги и очищаем память юзера
    await callback.answer()
    await callback.message.answer(
        text=f"Саламуля!\n"
             f"Это бот с поддержкой Chat GPT\n"
             f"Ты можешь ему задать вопрос с помощью соответствующей кнопки\n"
             f"Любишь поиграть? Жми кнопку \"Квиз\"\n"
             f"Не с кем поболтать? Не проблема, жми кнопку \"Разговор\"\n"
             f"Хочешь узнать что-то новое? Бот насыпет тебе Фактов!\n"
             f"Нужно перевести какой-то текст? Ну, кнопку ты и так видишь )",
        reply_markup=kb1
    )