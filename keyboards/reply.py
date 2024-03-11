from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    KeyboardButtonPollType
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Смайлики"),
            KeyboardButton(text="Ссылки")
        ],
        [
            KeyboardButton(text="Калькулятор"),
            KeyboardButton(text="Спец. кнопки")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True
)

spec = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить геолокацию", request_location=True),
            KeyboardButton(text="Отправить контакт", request_contact=True)
        ],
        [
            KeyboardButton(text="Начать опрос/голосование", request_poll=KeyboardButtonPollType())
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True
)
