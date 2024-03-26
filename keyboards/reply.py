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
# 1C api keyboard
data = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💶 Счета")
        ],
        [
            KeyboardButton(text="📊 Транзакции")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Какие данные хотите получить",
    selective=True
)

transactions = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💳 Получить транзакции"),
            KeyboardButton(text="➕ Создать транзакцию")
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True,
)

income = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📈 По доходам"),
         KeyboardButton(text="📉 По расходам")],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите тип",
    selective=True
)

account = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🧾 Получить счета"),
            KeyboardButton(text="➕ Создать счет")
        ],
        [
            KeyboardButton(text="🗞 Типы")
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True
)

income_expenses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📈 Доходы"),
            KeyboardButton(text="📉 Расходы")
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True
)

create_type_income = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕ Создать тип доходов"),
            KeyboardButton(text="🧾 Получить типы доходов")
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True
)

create_type_expenses = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="➕ Создать тип расходов"),
            KeyboardButton(text="🧾 Получить типы расходов")
        ],
        [
            KeyboardButton(text="🔙 Назад")
        ]
    ],
    resize_keyboard=True
)

types = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📈 Типы доходов"),
            KeyboardButton(text="📉 Типы расходов")
        ]
    ],
    resize_keyboard=True
)
