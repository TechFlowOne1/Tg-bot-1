from aiogram import types


button1 = types.KeyboardButton(text = "Старт")
button2 = types.KeyboardButton(text = "Инфо")
button3 = types.KeyboardButton(text = "Лиса")
button4 = types.KeyboardButton(text = "Проф")
button5 = types.KeyboardButton(text = "кнопка 5")
button6 = types.KeyboardButton(text = "кнопка 6")
button7 = types.KeyboardButton(text = "кнопка 7")

keyboard1 = [
    [button1, button2, button3],
    [button4, button5, button6],
    [button7],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)