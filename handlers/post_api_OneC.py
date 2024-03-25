import aiohttp

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message
from handlers.commands import find_name_by_id
from handlers.get_api_OneC import get_account, get_type
from keyboards import reply

post_api_router = Router()


# Создать счет
@post_api_router.message(F.text == "➕ Создать счет")
async def post_account(message: Message, state: FSMContext):
    await message.answer("Введите название счета")
    await state.set_state("название")


@post_api_router.message(StateFilter("название"), F.text)
async def state_account(message: Message, state: FSMContext):
    accounts_code = {}
    accounts_data = await get_account(message)
    account = str(message.text)
    for i in accounts_data:
        accounts_code[i["nameAccount"]] = i["code"]
    if account in accounts_code:
        return await message.answer("Такой счет уже существует")
    await state.update_data({"account": account})
    await message.answer("Введите сумму счета")
    await state.set_state("сумма_счета")


@post_api_router.message(StateFilter("сумма_счета"))
async def state_sum(message: Message, state: FSMContext):
    amount = (message.text)
    if not amount.isdigit():
        return await message.answer("Введите сумму только из чисел")
    data = await state.get_data()
    account = data.get("account")

    # print(amount, account)
    user_id = message.from_user.id
    name = find_name_by_id(user_id)
    url = "https://fg.shopfigaro.com/shamil/hs/account/oneAccount"
    data = {
        "nameAccount": account,
        "userName": name,
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
    accounts_code = {}
    accounts_data = await get_account(message)
    account = str(message.text)
    for i in accounts_data:
        accounts_code[i["nameAccount"]] = i["code"]
    if account in accounts_code:
        account_code = accounts_code[account]
        await state.update_data({"account_code": account_code})
    else:
        return await message.answer("Такого счета не существует")

    await message.answer("Укажите тип транзакции")
    await state.set_state("тип")


@post_api_router.message(StateFilter("тип"))
async def state_type(message: Message, state: FSMContext):
    type_income_code = {}
    type_income_data = await get_type(message)
    type_income = str(message.text)
    for i in type_income_data:
        type_income_code[i["nameType"]] = i["code"]
    if type_income in type_income_code:
        type_income_code = type_income_code[type_income]
        await state.update_data({"type_income": type_income})
    else:
        return await message.answer(f'Такого типа не существует\nХотите его создать?', reply_markup=reply.create_type_income)
    await message.answer("Укажите сумму")
    await state.set_state("сумма транзакции")


@post_api_router.message(StateFilter("сумма транзакции"))
async def state_sum(message: Message, state: FSMContext):
    summ = int(message.text)
    await state.update_data({"summ": summ})
    await message.answer("Добавьте описание")
    await state.set_state("описание")


@post_api_router.message(StateFilter("описание"))
async def state__description_expenses(message: Message, state: FSMContext):
    description = str(message.text)
    data = await state.get_data()
    account = data.get("account_code")
    typee = data.get("type_income")
    summ = data.get("summ")

    user_id = message.from_user.id
    name = find_name_by_id(user_id)
    url = "https://fg.shopfigaro.com/shamil/hs/postTransactions/transactionIncome"
    data = {
        "userName": name,
        "nameAccount": account,
        "type": typee,
        "sum": summ,
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
    accounts_code = {}
    accounts_data = await get_account(message)
    account = str(message.text)
    for i in accounts_data:
        accounts_code[i["nameAccount"]] = i["code"]
    if account in accounts_code:
        account_code = accounts_code[account]
        await state.update_data({"account_code": account_code})
    else:
        return await message.answer("Такого счета не существует")
    print(accounts_code)
    await message.answer("Укажите тип транзакции")
    await state.set_state("тип расходов")


@post_api_router.message(StateFilter("тип расходов"))
async def state_type_expenses(message: Message, state: FSMContext):
    typee = str(message.text)
    await state.update_data({"typee": typee})
    await message.answer("Укажите сумму")
    await state.set_state("сумма транзакции расходов")


@post_api_router.message(StateFilter("сумма транзакции расходов"))
async def state_sum_expenses(message: Message, state: FSMContext):
    summ = int(message.text)
    await state.update_data({"summ": summ})
    await message.answer("Добавьте описание")
    await state.set_state("описание расходов")


@post_api_router.message(StateFilter("описание расходов"))
async def state_description_expenses(message: Message, state: FSMContext):
    description = str(message.text)
    data = await state.get_data()
    account = data.get("account_code")
    print(account)
    typee = data.get("typee")
    summ = data.get("summ")
    user_id = message.from_user.id
    name = find_name_by_id(user_id)

    url = "https://fg.shopfigaro.com/shamil/hs/postTransactions/transactionExpenses"
    data = {
        "userName": name,
        "nameAccount": account,
        "type": typee,
        "sum": summ,
        "description": description
    }
    print(data)
    connector = aiohttp.TCPConnector(ssl=False)

    async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth("Shamil", "123"),
            connector=connector
    ) as session:
        async with session.post(url=url, json=data) as resp:
            if resp.status == 406:
                return message.answer(f'Недостаточно средст на счету', reply_markup=reply.data)
            elif resp.status == 200:
                await message.answer("Транзакция прошла успешно", reply_markup=reply.data)
    # print(data)
    await state.clear()



