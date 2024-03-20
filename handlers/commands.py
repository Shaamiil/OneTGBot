import sqlite3
import types

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from keyboards import reply

commands_router = Router()

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
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

@commands_router.message(StateFilter("имя"))
async def save_name(message: Message, state: FSMContext):
    name = message.text
    cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
    conn.commit()
    await message.answer(f'Имя "{name}" успешно сохранено в базе данных.')
