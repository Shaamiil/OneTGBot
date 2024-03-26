import aiohttp

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message
from handlers.commands import find_name_by_id
from handlers.get_api_OneC import get_type, get_type_expenses
from keyboards import reply

type_router = Router()


# Получить все типы доходов
@type_router.message(F.text == "🧾 Получить типы доходов")
async def get_type_income(message):
    types = ""
    types_income = await get_type(message)
    for i in types_income:
        types += f'{i["nameType"]}\n'
    await message.answer(types)

# Получить все типы расходов
@type_router.message(F.text == "🧾 Получить типы расходов")
async def gett_type_expenses(message):
    types = ""
    types_expenses = await get_type_expenses(message)
    for i in types_expenses:
        types += f'{i["nameType"]}'
    await message.answer(types)


# Создать тип доходов
@type_router.message(F.text == "➕ Создать тип доходов")
async def create_types(message: Message, state: FSMContext):
    await message.answer("Введите название типа")
    await state.set_state("название типа дохода")


@type_router.message(StateFilter("название типа дохода"))
async def create_type_income(message: Message, state: FSMContext):
    type_income_code = {}
    type_income_data = await get_type(message)
    type_income = message.text
    for item in type_income_data:
        if item["nameType"] == type_income:
            return await message.answer("Такой тип уже существует")
    user_id = message.from_user.id
    name = find_name_by_id(user_id)
    url = "https://fg.shopfigaro.com/shamil/hs/type/incomePOST"
    data = {
        "nameType": type_income,
        "userName": name,
    }
    connector = aiohttp.TCPConnector(ssl=False)

    async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth("Shamil", "123"),
            connector=connector
    ) as session:
        async with session.post(url=url, json=data) as resp:
            if resp.status != 200:
                return message.answer(f'Тип не создан\nХз почему')

    await message.answer("Тип успешно создан", reply_markup=reply.data)
    await state.clear()


# Создать тип расходов
@type_router.message(F.text == "➕ Создать тип расходов")
async def create_types(message: Message, state: FSMContext):
    await message.answer("Введите название типа")
    await state.set_state("название типа расхода")


@type_router.message(StateFilter("название типа расхода"))
async def create_type_expenses(message: Message, state: FSMContext):
    type_expenses_code = {}
    type_expenses_data = await get_type_expenses(message)
    type_expenses = message.text
    for item in type_expenses_data:
        if item["nameType"] == type_expenses:
            return await message.answer("Такой тип уже существует")
    user_id = message.from_user.id
    name = find_name_by_id(user_id)
    url = "https://fg.shopfigaro.com/shamil/hs/type/expensesPOST"
    data = {
        "nameType": type_expenses,
        "userName": name,
    }
    connector = aiohttp.TCPConnector(ssl=False)

    async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth("Shamil", "123"),
            connector=connector
    ) as session:
        async with session.post(url=url, json=data) as resp:
            if resp.status != 200:
                return message.answer(f'Тип не создан\nХз почему')

    await message.answer("Тип успешно создан", reply_markup=reply.data)
    await state.clear()