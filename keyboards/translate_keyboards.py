from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Выбор языков

lang_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="English 🇺🇸", callback_data="lang_en"),
            InlineKeyboardButton(text="Español 🇪🇸", callback_data="lang_es")
        ],
        [
            InlineKeyboardButton(text="Deutsch 🇩🇪", callback_data="lang_de"),
            InlineKeyboardButton(text="Français 🇫🇷", callback_data="lang_fr")
        ]
    ]
)

# Панель под результатом перевода

translate_control_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Сменить язык 🔄", callback_data="translate_change"),
            InlineKeyboardButton(text="Закончить ❌", callback_data="translate_finish")
        ]
    ]
)