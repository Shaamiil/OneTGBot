from aiogram.utils.keyboard import ReplyKeyboardBuilder

def calc():
    buttons = [
        "1", "2", "3", "/",
        "4", "5", "6", "*",
        "7", "8", "9", "-",
        "0", ".", "=", "+",
    ]

    builder = ReplyKeyboardBuilder()
    for item in buttons:
        builder.button(text=item)
    builder.button(text="Назад")
    builder.adjust(*[4] * 4)

    return builder.as_markup(resize_keyboard=True)