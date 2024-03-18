import asyncio
import datetime

import requests
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import message
import aiohttp

# Ваш токен бота
API_TOKEN = '6654806222:AAEIbQi8mminaJKPkUtfLggJeKbmZrK2tvw'
# Ваш API ключ для OpenWeatherMap
API_KEY = '436545b7f7083fe5d098294c296ff748'
# ID вашего чата в Telegram
CHAT_ID = '1841823603'
# Город, погоду которого вы хотите получать
CITY = 'Makhachkala'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def get_weather():
    async with aiohttp.ClientSession() as session:
        resultat = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric').json()
        weather_msg = (f'<b>🌡️ Температура:</b>  {resultat["main"]["temp"]} °C'
                       f'\n<b>🤒 Ощущается как:</b> {resultat["main"]["feels_like"]} °C'
                       f'\n<b>🌬️ Скорость ветра:</b>  {resultat["wind"]["speed"]} м/с'
                       f'\n<b>💧 Влажность:</b>  {resultat["main"]["humidity"]}%')

        await message.answer(weather_msg, parse_mode='HTML')


async def send_weather(weather_msg=None):
    weather = await get_weather()
    await bot.send_message(chat_id=CHAT_ID, text=weather_msg, parse_mode=ParseMode.HTML)


async def scheduler():
    while True:
        now = datetime.datetime.now()
        if now.hour == 9 and now.minute == 0:
            await send_weather()
            await asyncio.sleep(86400)
