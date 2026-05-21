from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_button_gpt = InlineKeyboardButton(text="Спросить у GPT", callback_data="ask_gpt")
inline_button_ya = InlineKeyboardButton(text="Спросить у Yandex", callback_data="ask_yandex")

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[[inline_button_gpt, inline_button_ya]])


