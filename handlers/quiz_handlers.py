from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter
from services.chat_gpt import ask_gpt, user_history
from keyboards.quiz_keyboard import quiz_inline_keyboard, quiz_control_keyboard
from keyboards.keyboards import kb1, quiz_stop_keyboard

router = Router()

# Фулл хэндлеры для квиза пришлось делать с нейронкой, вернее под её руководством
# Слишком много зависимостей и подводных камней в которых я не смог разобраться сам
# Больше всего времени потрачено именно на эти хэндлеры - НЕ ВЫВОЖУ (буду отдельно учить)
# Из всего проекта наверное самая трудная часть!
# Запутался сильно в областях видимости (надо тоже подтягивать)


#Старт квиза

@router.message(Command("quiz"))
@router.message(F.text == "Квиз")
async def start_quiz_mode(message: Message, state: FSMContext):
    await state.clear()  # Принудительно гасим любые состояния из других режимов (например если нажимали GPT)
    await message.answer("Запускаю квиз...", reply_markup=ReplyKeyboardRemove())
    await message.answer("Секунду, подгружаю темы для квиза...", reply_markup=quiz_stop_keyboard)

    #Достаём заготовленную фотку из "assets"
    photo = FSInputFile("assets/quiz.jpg")

    await message.answer_photo(
        photo=photo,
        caption="Добро пожаловать в интеллектуальный квиз! 🧠\nВыбери тему, которая тебе интересна:",
        reply_markup=quiz_inline_keyboard
    )


#Обработка инлайн кнопок

@router.callback_query(F.data.startswith("quiz_"))
async def choose_quiz_topic(callback: CallbackQuery):
    user_key = f"quiz_{callback.from_user.id}"
    action = callback.data

    # Кнопка "Закончить квиз"
    if action == "quiz_finish":
        score = user_history.get(user_key, {}).get("score", 0)
        user_history[user_key] = None  # Полностью сбрасываем сессию

        await callback.message.answer(
            text=f"Квиз окончен! Твой финальный счёт: {score} 🏆\nВозвращаюсь в главное меню.",
            reply_markup=kb1
        )
        await callback.answer()
        return

    # Кнопка "Сменить тему"
    if action == "quiz_change":
        await callback.message.answer(
            text="Выбери новую тему для квиза:",
            reply_markup=quiz_inline_keyboard
        )
        await callback.answer()
        return

    # Список доступных тем
    topics = {
        "quiz_space": "Космос 🚀",
        "quiz_movies": "Фильмы 🎬",
        "quiz_music": "Музыка 🎵",
        "quiz_games": "Игры 🎮"
    }

    # Список для хранения уже заданных вопросов. Крайне важно! Без списка получается чушь!!!
    used_questions = []

    # Если нажали "Еще вопрос" берем старую тему и историю
    if action == "quiz_more":
        if user_key not in user_history or not user_history[user_key]:
            await callback.message.answer("Сессия квиза потеряна. Начни заново через /quiz")
            await callback.answer()
            return
        current_topic = user_history[user_key]["topic"]
        used_questions = user_history[user_key]["messages"]
    else:
        # Если выбрали новую тему, создаем чистую структуру, но сохраняем набранный счет. Абуз поинтов?))
        current_topic = topics[action]
        user_history[user_key] = {
            "topic": current_topic,
            "score": user_history.get(user_key, {}).get("score", 0),
            "messages": []
        }

    await callback.answer()
    await callback.message.answer("Генерирую вопрос...")

    # Базовый промпт для нейронки как ведущего викторины
    prompt = (
        f"Ты ведущий викторины. Задай один интересный вопрос средней сложности на тему '{current_topic}'. "
        f"ВАЖНО! Напиши ТОЛЬКО сам вопрос. Никаких приветствий, вариантов ответа или лишнего текста."
        f"Не задавай слишком банальные вопросы и главное не повторяйся"
        f"Если пользователь отвечает верно на 5 вопросов подряд, увеличь сложность на 25%"
    )

    # Если в этой сессии уже были вопросы добавляем их списком в промпт как жесткое исключение
    # Иначе вопросы начинают повторяться и квиз изичный
    if used_questions:
        formatted_exceptions = "\n".join([f"- {q}" for q in used_questions])
        prompt += f"\n\nКРИТИЧЕСКИ ВАЖНО! Никогда не задавай вопросы, которые уже были. Вот их список:\n{formatted_exceptions}"

    # Делаем запрос к GPT через временный ключ чтобы не захламлять контекст
    # Это списал у нейронки, потому что не знал как пофиксить проблему
    temp_key = f"temp_{user_key}"
    question = await ask_gpt(user_id=temp_key, user_message=prompt)
    user_history[temp_key] = []

    # Сохраняем свежий вопрос в список уже использованных. ОБЯЗАТЕЛЬНО
    user_history[user_key]["messages"].append(question)

    # Выводим вопрос юзеру и убираем реплай клавиатуру. Иначе не удобно
    await callback.message.answer(text=question, reply_markup=ReplyKeyboardRemove())

@router.message(F.text == "Закончить квиз", StateFilter("*"))
async def exit_quiz_mode_reply(message: Message, state: FSMContext):
    user_key = f"quiz_{message.from_user.id}"
    user_history[user_key] = None
    await state.clear()
    await message.answer(
        text="Квиз окончен! Возвращаюсь в главное меню.",
        reply_markup=kb1
    )


#Хватаем ответ пользователя и обрабатываем

@router.message(F.text)
async def handle_quiz_answer(message: Message):
    user_key = f"quiz_{message.from_user.id}"

    # Проверяем идет ли сейчас у пользователя квиз
    if user_key in user_history and user_history[user_key] is not None:

        # Текстовая подстраховка для выхода
        if message.text == "Закончить квиз":
            score = user_history[user_key]["score"]
            user_history[user_key] = None
            await message.answer(f"Квиз окончен! Твой финальный счёт: {score} 🏆\nВозвращаюсь в главное меню.",
                                 reply_markup=kb1)
            return

        saved_messages = user_history[user_key]["messages"]
        if not saved_messages:
            return

        # Берем самый последний заданный вопрос из списка
        last_question = saved_messages[-1]

        await message.answer("Проверяю твой ответ... 🔍")

        # Промпт для проверки ответа пользователя
        check_prompt = (
            f"Был задан вопрос: '{last_question}'. "
            f"Пользователь ответил: '{message.text}'. "
            f"Оцени, правильный ли ответ. Твой ответ должен начинаться строго со слова 'ДА' или 'НЕТ', "
            f"а после этого слова напиши в одно короткое предложение правильный ответ или пояснение."
        )

        temp_key = f"temp_check_{user_key}"
        gpt_analysis = await ask_gpt(user_id=temp_key, user_message=check_prompt)
        user_history[temp_key] = []  # Чистим времянку проверки

        # Проверяем вердикт нейронки
        if gpt_analysis.strip().upper().startswith("ДА"):
            user_history[user_key]["score"] += 1
            result_text = f"✅ **Правильно!**\n\n"
        else:
            result_text = f"❌ **Не совсем так...**\n\n"

        current_score = user_history[user_key]["score"]
        result_text += f"{gpt_analysis}\n\n🏆 Текущий счёт: {current_score}"

        # Отправляем результат проверки и инлайн клавиатуру управления квизом
        await message.answer(text=result_text, reply_markup=quiz_control_keyboard)

    else:
        # Если квиз не запущен просто игнорируем и пускаем сообщение дальше в эхо бот
        return