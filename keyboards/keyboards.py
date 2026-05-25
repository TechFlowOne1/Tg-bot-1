from aiogram import types

button1 = types.KeyboardButton(text="Старт")
button2 = types.KeyboardButton(text="Инфо")
button3 = types.KeyboardButton(text="Задать вопрос GPT")
button4 = types.KeyboardButton(text="Выйти из режима GPT")

keyboard1 = [
    [button1, button2, button3],
]

keyboard2 = [
    [button4],
]


kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
gpt_exit_keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)