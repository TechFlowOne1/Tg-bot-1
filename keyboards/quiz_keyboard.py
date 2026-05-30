from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура для выбора темы квиза
quiz_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Космос 🚀", callback_data="quiz_space"),
            InlineKeyboardButton(text="Фильмы 🎬", callback_data="quiz_movies")
        ],
        [
            InlineKeyboardButton(text="Музыка 🎵", callback_data="quiz_music"),
            InlineKeyboardButton(text="Игры 🎮", callback_data="quiz_games")
        ]
    ]
)

# Кнопки управления квизом после ответа пользователя
quiz_control_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ещё вопрос 🔄", callback_data="quiz_more"),
            InlineKeyboardButton(text="Сменить тему 📋", callback_data="quiz_change")
        ],
        [
            InlineKeyboardButton(text="Закончить квиз ❌", callback_data="quiz_finish")
        ]
    ]
)