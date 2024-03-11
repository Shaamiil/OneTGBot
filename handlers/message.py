import requests
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message

from keyboards import builders, inline, reply

message_router = Router()
key = '436545b7f7083fe5d098294c296ff748'

@message_router.message(F.text == "Узнать погоду")
async def weather(message: Message, state: FSMContext):
    await message.answer("Введите город")
    await state.set_state("город")

    await state.update_data(command=message.text)


@message_router.message(F.text)
async def echo(message: Message):
    msg = message.text.lower()
    if msg == "ссылки":
       await message.answer("Вот ваши ссылки:", reply_markup=inline.dop)
    elif msg == "спец. кнопки":
        await message.answer("Ваши спец. кнопки", reply_markup=reply.spec)
    elif msg == "калькулятор":
        await message.answer("Введите значение", reply_markup=builders.calc())


@message_router.message(StateFilter("город"))
async def get_weather(message: Message, state: FSMContext):
    print(1)
    city = message.text.strip().lower()
    resultat = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric').json()
    if resultat["cod"] != 200:
        return await message.answer("Город не найден")

    weather_msg = (f'<b>🌡️ Температура:</b>  {resultat["main"]["temp"]} °C'
                   f'\n<b>🤒 Ощущается как:</b> {resultat["main"]["feels_like"]} °C'
                   f'\n<b>🌬️ Скорость ветра:</b>  {resultat["wind"]["speed"]} м/с'
                   f'\n<b>💧 Влажность:</b>  {resultat["main"]["humidity"]}%')

    await message.answer( weather_msg, parse_mode='HTML')

    state_data = await state.get_data()
    asd = state_data.get("command")

    await state.clear()
