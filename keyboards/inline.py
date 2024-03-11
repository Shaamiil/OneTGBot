from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

dop = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Dota 2", url="https://dota2.com"),
            InlineKeyboardButton(text="1C ИТС", url="https://its.1c.ru/")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите ссылку",
    selective=True
)