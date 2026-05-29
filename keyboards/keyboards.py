from aiogram import types

button1 = types.KeyboardButton(text="Старт")
button2 = types.KeyboardButton(text="Инфо")

button3 = types.KeyboardButton(text="Задать вопрос GPT")
button4 = types.KeyboardButton(text="Выйти из режима GPT")

button5 = types.KeyboardButton(text="Рандомный факт")
button6 = types.KeyboardButton(text="Ещё факт")
button7 = types.KeyboardButton(text="Закончить")

button8 = types.KeyboardButton(text="Разговор")



keyboard1 = [
    [button1, button2, button3],
    [button5, button8],
]

keyboard2 = [
    [button4],
]

keyboard3 = [
    [button6, button7],
]


kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)

gpt_exit_keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)

fact_keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard3, resize_keyboard=True)
