import sqlite3

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from keyboards import reply
from keyboards.reply import data

commands_router = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, name TEXT)')
conn.commit()


@commands_router.message(Command("startt"))
async def start(message: Message):
    await message.answer(
        text=f'Привет, {message.from_user.first_name}',
        reply_markup=reply.main
    )


@commands_router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer('Привет! Введите ваше имя.')
    await state.set_state("имя")


@commands_router.message(StateFilter("имя"), F.text)
async def save_name(message: Message, state: FSMContext):
    name = message.text
    if not name.isalpha():
        return await message.answer("Введите имя без лишних символов")
    user_id = message.from_user.id
    cursor.execute('INSERT INTO users (user_id, name) VALUES (?,?)', (user_id, name,))
    conn.commit()
    await message.answer(f'Имя "{name}" успешно сохранено в базе данных.', reply_markup=data)
    await state.clear()


def find_name_by_id(user_id):

    cursor.execute('SELECT name FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()

    if result:
        name = result[0]
        return name
    else:
        return ""