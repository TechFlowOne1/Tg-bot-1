from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command
from services.chat_gpt import ask_gpt, user_history
from keyboards.inline_keyboard import talk_inline_keyboard, talk_finish_keyboard
from keyboards.keyboards import kb1

router = Router()

@router.message(Command("talk"))
@router.message(F.text == "Разговор")
async def start_talk_mode(message: Message):
    await message.answer("Ван момент, подгружаю список персонажей...")

    photo = FSInputFile("assets/talk.jpg")

    await message.answer_photo(
        photo=photo,
        caption="Есть вопросы к этим ребятам? Выбери персонажа:",
        reply_markup=talk_inline_keyboard
    )


@router.callback_query(F.data.startswith("talk_"))
async def choose_character(callback: CallbackQuery):
    user_key = f"talk_{callback.from_user.id}"

    selected_hero = callback.data

    if selected_hero == "talk_finish":
        user_history[user_key] = []
        await callback.message.answer(
            text="Диалог завершен. Возвращаюсь в главное меню!",
            reply_markup=kb1
        )
        await callback.answer()
        return

    prompts = {
        "talk_stark": "Ты Тони Старк (Железный Человек). Отвечай харизматично, с сарказмом, используй долю эгоизма, но оставайся гением. Общайся на 'ты'.",
        "talk_banner": "Ты Брюс Беннер (Халк). Отвечай как гениальный, скромный, немного уставший ученый-физик. Сдерживай внутренние эмоции, будь вежлив.",
        "talk_tchalla": "Ты Т'Чалла (Черная Пантера), король Ваканды. Твои ответы мудрые, величественные, благородные и уважительные. Ваканда навеки!",
        "talk_natasha": "Ты Наташа Романофф (Черная Вдова). Отвечай прямолинейно, но как профессиональный шпион. В ответах чувствуется уверенность."
    }

    user_history[user_key] = [
        {"role": "system", "content": prompts[selected_hero]}
    ]

    greetings = {
        "talk_stark": "Я Тони Старк. Да-да, гений, миллиардер, плейбой, ну ты знаешь... Вопросы?",
        "talk_banner": "Привет. Меня зовут Брюс. У тебя есть 5 минут, пока я в настроении...",
        "talk_tchalla": "Приветствую тебя, друг мой. Я Т'Чалла, правитель Ваканды. О чем желаешь поговорить?",
        "talk_natasha": "Привет. Я Наташа. Давай сразу к делу, шпионские игры оставим на потом."
    }

    await callback.answer()
    await callback.message.answer(text=greetings[selected_hero])

    @router.message(F.text)
    async def handle_talk_message(message: Message):
        user_key = f"talk_{message.from_user.id}"

        if user_key in user_history and user_history[user_key]:

            if message.text == "Закончить":
                user_history[user_key] = []
                await message.answer("Диалог завершен. Возвращаюсь в главное меню!", reply_markup=kb1)
                return

            await message.answer("Думаю...")

            reply = await ask_gpt(user_id=user_key, user_message=message.text)

            await message.answer(text=reply, reply_markup=talk_finish_keyboard)

        else:
            return