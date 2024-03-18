import aiohttp
import json
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message
from keyboards import reply

post_api_router = Router()


# Создать счет
@post_api_router.message(F.text == "➕ Создать счет")
async def post_account(message: Message, state: FSMContext):
    await message.answer("Введите название счета")
    await state.set_state("название")


@post_api_router.message(StateFilter("название"))
async def state_account(message: Message, state: FSMContext):
    account = str(message.text)
    await state.update_data({"account": account})
    await message.answer("Введите сумму счета")
    await state.set_state("сумма_счета")


@post_api_router.message(StateFilter("сумма_счета"))
async def state_sum(message: Message, state: FSMContext):
    amount = int(message.text)
    data = await state.get_data()
    account = data.get("account")

    # print(amount, account)
    url = "https://fg.shopfigaro.com/shamil/hs/account/oneAccount"
    data = {
        "nameAccount": account,
        "sum": amount
    }
    connector = aiohttp.TCPConnector(ssl=False)

    async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth("Shamil", "123"),
            connector=connector
    ) as session:
        async with session.post(url=url, json=data) as resp:
            if resp.status != 200:
                return message.answer(f'Счет не создан\nХз почему')

    await message.answer("Счет успешно создан", reply_markup=reply.data)
    # print(data)
    await state.clear()


# Создать транзакцию доходов
@post_api_router.message(F.text == "📈 Доходы")
async def post_transaction_income(message: Message, state: FSMContext):
    await message.reply("Введите название своего счета")
    await state.set_state("название транзакции")


@post_api_router.message(StateFilter("название транзакции"))
async def state_account(message: Message, state: FSMContext):
    account = str(message.text)
    await state.update_data({"account": account})
    await message.answer("Укажите тип транзакции")
    await state.set_state("тип")


@post_api_router.message(StateFilter("тип"))
async def state_type(message: Message, state: FSMContext):
    typee = str(message.text)
    await state.update_data({"type": typee})
    await message.answer("Укажите сумму")
    await state.set_state("сумма транзакции")


@post_api_router.message(StateFilter("сумма транзакции"))
async def state_sum(message: Message, state: FSMContext):
    sum = int(message.text)
    await state.update_data({"sum": sum})
    await message.answer("Добавьте описание")
    await state.set_state("описание")


@post_api_router.message(StateFilter("описание"))
async def state__description_expenses(message: Message, state: FSMContext):
    description = str(message.text)
    data = await state.get_data()
    account = data.get("account")
    typee = data.get("typee")
    sum = data.get("sum")

    url = "https://fg.shopfigaro.com/shamil/hs/postTransactions/transactionIncome"
    data = {
        "nameAccount": account,
        "type": typee,
        "sum": sum,
        "description": description
    }
    # print(data)
    connector = aiohttp.TCPConnector(ssl=False)

    async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth("Shamil", "123"),
            connector=connector
    ) as session:
        async with session.post(url=url, json=data) as resp:
            if resp.status != 200:
                return message.answer(f'Транзакция не прошла\nХз почему')

    await message.answer("Транзакция прошла успешно", reply_markup=reply.data)
    # print(data)
    await state.clear()


# Создать транзакцию расходов
@post_api_router.message(F.text == "📉 Расходы")
async def post_transaction_expenses(message: Message, state: FSMContext):
    await message.reply("Введите название своего счета")
    await state.set_state("название транзакции расходов")


@post_api_router.message(StateFilter("название транзакции расходов"))
async def state_account_expenses(message: Message, state: FSMContext):
    account = str(message.text)
    await state.update_data({"account": account})
    await message.answer("Укажите тип транзакции")
    await state.set_state("тип расходов")


@post_api_router.message(StateFilter("тип расходов"))
async def state_type_expenses(message: Message, state: FSMContext):
    typee = str(message.text)
    await state.update_data({"type": typee})
    await message.answer("Укажите сумму")
    await state.set_state("сумма транзакции расходов")


@post_api_router.message(StateFilter("сумма транзакции расходов"))
async def state_sum_expenses(message: Message, state: FSMContext):
    sum = int(message.text)
    await state.update_data({"sum": sum})
    await message.answer("Добавьте описание")
    await state.set_state("описание расходов")


@post_api_router.message(StateFilter("описание расходов"))
async def state_description_expenses(message: Message, state: FSMContext):
    description = str(message.text)
    data = await state.get_data()
    account = data.get("account")
    typee = data.get("typee")
    sum = data.get("sum")

    url = "https://fg.shopfigaro.com/shamil/hs/postTransactions/transactionExpenses"
    data = {
        "nameAccount": account,
        "type": typee,
        "sum": sum,
        "description": description
    }
    # print(data)
    connector = aiohttp.TCPConnector(ssl=False)

    async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth("Shamil", "123"),
            connector=connector
    ) as session:
        async with session.post(url=url, json=data) as resp:
            if resp.status == 406:
                return message.answer(f'Недостаточно средст на счету')
            elif resp.status == 200:
                await message.answer("Транзакция прошла успешно", reply_markup=reply.data)
    # print(data)
    await state.clear()
