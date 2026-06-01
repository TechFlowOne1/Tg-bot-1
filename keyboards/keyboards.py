from aiogram import types

button1 = types.KeyboardButton(text="Старт")

button3 = types.KeyboardButton(text="Задать вопрос GPT")
button4 = types.KeyboardButton(text="Выйти из режима GPT")

button5 = types.KeyboardButton(text="Рандомный факт")
button6 = types.KeyboardButton(text="Ещё факт")
button7 = types.KeyboardButton(text="Закончить")

button8 = types.KeyboardButton(text="Разговор")

button9 = types.KeyboardButton(text="Квиз")

# Я подумал, избавиться от кнопки ИНФО (она была button2) и тупо сделать кнопку СТАРТ сразу с приветствием и всей инфой
# Что бы помимо кнопки СТАРТ не было других кнопок и пользователь сразу прочитал информацию о боте
# По этому нумерация исключает button2 (она не потерялась, я её выпилил)

start_keyboard_layout = [
    [button1]
]

main_keyboard_layout = [
    [button3, button5],
    [button8, button9]
]

keyboard2 = [
    [button4],
]

keyboard3 = [
    [button6, button7],
]

# Собираем все клавиатуры

start_kb = types.ReplyKeyboardMarkup(keyboard=start_keyboard_layout, resize_keyboard=True, one_time_keyboard=True)

kb1 = types.ReplyKeyboardMarkup(keyboard=main_keyboard_layout, resize_keyboard=True)

gpt_exit_keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)

fact_keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard3, resize_keyboard=True)
