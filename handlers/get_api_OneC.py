import aiohttp
from aiogram import Router, F
from aiogram.types import Message

from handlers.commands import find_name_by_id

get_api_router = Router()


async def get_account(message: Message):
    url = "https://fg.shopfigaro.com/shamil/hs/account/allAccount"
    user_id = message.from_user.id
    name = find_name_by_id(user_id)
    data = {
        "userName": name
    }
    connector = aiohttp.TCPConnector(ssl=False)

    async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth("Shamil", "123"),
            connector=connector
    ) as session:
        async with session.post(url=url, json=data) as resp:
            resp_data = await resp.read()
            import json
            resp_json = json.loads(resp_data)
            return resp_json


async def get_type(message: Message):
    url = "https://fg.shopfigaro.com/shamil/hs/type/income"
    user_id = message.from_user.id
    name = find_name_by_id(user_id)
    data = {
        "userName": name
    }
    connector = aiohttp.TCPConnector(ssl=False)

    async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth("Shamil", "123"),
            connector=connector
    ) as session:
        async with session.post(url=url, json=data) as resp:
            resp_data = await resp.read()
            import json
            resp_json = json.loads(resp_data)
            # print(resp_json)
            return resp_json


# Получить счета
@get_api_router.message(F.text == "🧾 Получить счета")
async def get_wallets_message(message):
    account = ""
    accounts = await get_account(message)
    for i in accounts:
        account += f'{i["nameAccount"]}:  {str(i["sum"])}\n'
    # print(account)
    await message.answer(account)


# Получить транзакции
@get_api_router.message(F.text == "📈 По доходам")
async def get_income(message: Message):
    url = "https://fg.shopfigaro.com/shamil/hs/getTransactions/allTransactionsIncome"
    user_id = message.from_user.id
    name = find_name_by_id(user_id)
    data = {
        "userName": name
    }
    connector = aiohttp.TCPConnector(ssl=False)

    async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth("Shamil", "123"),
            connector=connector
    ) as session:
        async with session.get(url=url, json=data) as resp:
            resp_data = await resp.read()
            import json
            # print(resp_data)
            resp_json = json.loads(resp_data)
            # print(resp_json)
    transactions = ""
    for i in resp_json:
        transactions += f'✅{i["nameAccount"]}: {str(i["sum"])}\nОписание: {i["description"]}\n\n'
    await message.answer(transactions)


@get_api_router.message(F.text == "📉 По расходам")
async def get_consumption(message: Message):
    url = "https://fg.shopfigaro.com/shamil/hs/getTransactions/allTransactionsConsumption"
    user_id = message.from_user.id
    name = find_name_by_id(user_id)
    data = {
        "userName": name
    }
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth("Shamil", "123"),
            connector=connector
    ) as session:
        async with session.get(url=url, json=data) as resp:
            resp_data = await resp.read()
            import json
            # print(resp_data)
            resp_json = json.loads(resp_data)
            # print(resp_json)
    consumption = ""
    for i in resp_json:
        consumption += f'❎{i["nameAccount"]}: {str(i["sum"])}\nОписание: {i["description"]}\n\n'
    await message.answer(consumption)


