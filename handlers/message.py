import aiohttp
import requests
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter, Command
from aiogram.types import Message

from keyboards import builders, inline, reply

message_router = Router()
key = '436545b7f7083fe5d098294c296ff748'


@message_router.message(F.text.lower() == "Узнать погоду")
async def weather(message: Message, state: FSMContext):
    await message.answer("Введите город")
    await state.set_state("город")

    await state.update_data(command=message.text)


@message_router.message(F.text.lower() == "ссылки")
async def echo(message: Message):
    await message.answer("Cпец. кнопки:", reply_markup=inline.dop)


@message_router.message(F.text.lower() == "ссылки")
async def echo(message: Message):
    await message.answer("ваши спец. кнопки", reply_markup=reply.spec)


@message_router.message(F.text.lower() == "калькулятор")
async def echo(message: Message):
    await message.answer("Введите значение", reply_markup=builders.calc())


@message_router.message(StateFilter("город"))
async def get_weather(message: Message, state: FSMContext):
    city = message.text.strip().lower()
    resultat = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric').json()
    if resultat["cod"] != 200:
        return await message.answer("Город не найден")

    weather_msg = (f'<b>🌡️ Температура:</b>  {resultat["main"]["temp"]} °C'
                   f'\n<b>🤒 Ощущается как:</b> {resultat["main"]["feels_like"]} °C'
                   f'\n<b>🌬️ Скорость ветра:</b>  {resultat["wind"]["speed"]} м/с'
                   f'\n<b>💧 Влажность:</b>  {resultat["main"]["humidity"]}%')

    await message.answer(weather_msg, parse_mode='HTML')

    state_data = await state.get_data()
    asd = state_data.get("command")

    await state.clear()


# Api 1C
@message_router.message(Command("start"))
async def data(message: Message):
    await message.answer(
        text=f'Привет, {message.from_user.first_name}\nВыберите данные',
        reply_markup=reply.data
    )


@message_router.message(F.text == "💶 Счета")
async def account(message: Message):
    await message.answer("Че хочешь", reply_markup=reply.account)


@message_router.message(F.text == "🔙 Назад")
async def account(message: Message):
    await message.answer("Главное меню 🏦", reply_markup=reply.data)


@message_router.message(F.text == "📊 Транзакции")
async def transactions(message):
    await message.answer("Че надо", reply_markup=reply.transactions)


@message_router.message(F.text == "💳 Получить транзакции")
async def transactions(message):
    await message.answer("Какие транзакции интерисуют?", reply_markup=reply.income)


@message_router.message(F.text == "➕ Создать транзакцию")
async def transactions_income_expenses(message):
    await message.answer("Выберите тип транзакций", reply_markup=reply.income_expenses)
