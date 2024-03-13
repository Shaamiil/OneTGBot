import aiohttp
import requests
from aiogram import Router, F
from aiogram.types import Message

get_api_router = Router()

# Получить счета
@get_api_router.message(F.text.lower() == "получить счета")
async def get_account(message: Message):
    url = "https://fg.shopfigaro.com/shamil/hs/account/allAccount"
    async with aiohttp.ClientSession(auth=aiohttp.BasicAuth("Shamil", "123")) as session:
        async with session.get(url) as resp:
            resp_data = await resp.read()
            import json
            resp_json = json.loads(resp_data)
            # print(resp_json)
    account = ""
    for i in resp_json:
        account += f'{i["nameAccount"]}:  {str(i["sum"])}\n'
    # print(account)
    await message.answer(account)

# Получить транзакции
@get_api_router.message(F.text.lower() == "по доходам")
async def get_income(message: Message):
    url = "https://fg.shopfigaro.com/shamil/hs/transactions/allTransactionsIncome"
    async with aiohttp.ClientSession(auth=aiohttp.BasicAuth("Shamil", "123")) as session:
        async with session.get(url) as resp:
            resp_data = await resp.read()
            import json
            # print(resp_data)
            resp_json = json.loads(resp_data)
            # print(resp_json)
    transactions = ""
    for i in resp_json:
        transactions += f'✅{i["nameAccount"]}: {str(i["sum"])}\nОписание: {i["description"]}\n\n'
    await message.answer(transactions)


@get_api_router.message(F.text.lower() == "по расходам")
async def get_consumption(message: Message):
    url = "https://fg.shopfigaro.com/shamil/hs/transactions/allTransactionsConsumption"
    async with aiohttp.ClientSession(auth=aiohttp.BasicAuth("Shamil", "123")) as session:
        async with session.get(url) as resp:
            resp_data = await resp.read()
            import json
            # print(resp_data)
            resp_json = json.loads(resp_data)
            # print(resp_json)
    consumption = ""
    for i in resp_json:
        consumption += f'❎{i["nameAccount"]}: {str(i["sum"])}\nОписание: {i["description"]}\n\n'
    await message.answer(consumption)
