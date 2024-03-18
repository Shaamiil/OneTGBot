from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards import reply

commands_router = Router()


@commands_router.message(Command("startt"))
async def start(message: Message):
    await message.answer(
        text=f'Привет, {message.from_user.first_name}',
        reply_markup=reply.main
    )
