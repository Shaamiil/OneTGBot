import asyncio
from aiogram import Bot, Dispatcher

from handlers import commands, message, get_api_OneC, post_api_OneC


async def main():
    bot = Bot("6654806222:AAEIbQi8mminaJKPkUtfLggJeKbmZrK2tvw")
    dp = Dispatcher()
    dp.include_routers(
        post_api_OneC.post_api_router,
        get_api_OneC.get_api_router,
        commands.commands_router,
        message.message_router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
