from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

talk_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Тони Старк", callback_data="talk_stark"),
            InlineKeyboardButton(text="Брюс Беннер", callback_data="talk_banner")
        ],
        [
            InlineKeyboardButton(text="Т'Чалла", callback_data="talk_tchalla"),
            InlineKeyboardButton(text="Наташа Романофф", callback_data="talk_natasha")
        ]
    ]
)

talk_finish_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Закончить", callback_data="talk_finish")
        ]
    ]
)