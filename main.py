import asyncio
from aiogram import Bot, Dispatcher

from handlers import commands, message


async def main():
    bot = Bot("6654806222:AAEIbQi8mminaJKPkUtfLggJeKbmZrK2tvw")
    dp = Dispatcher()
    dp.include_routers(
        commands.commands_router,
        message.message_router

    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)




if __name__ == '__main__':
    asyncio.run(main())