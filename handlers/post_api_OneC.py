import aiohttp
import requests
from aiogram import Router, F
from aiogram.types import Message

post_api_router = Router()

# Создать счет
@post_api_router.message(F.text.lower() == "создать счет")
async def post_account(message: Message):
    await message.reply("Сори, я такому еще не научился")