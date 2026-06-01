from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def make_row_keyboard(buttons: list[str]) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=button) for button in buttons]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)


# Так это у нас осталась с урока, но в проекте я никак не использовал
# Либо не нашел применения, либо просто не додумался, не знаю
# Решил оставить в коде на случай, если вдруг мне это понадобится
