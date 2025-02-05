from app.handlers import user, admin, payments
from app.utils import commands
from bot import bot, dp
import app.middlewares as middlewares

from app.database.models import async_main
from app.database.requests import init_admins

import asyncio
import logging

from aiogram.types import BotCommandScopeDefault



async def main():
    await async_main()
    await init_admins()

    logging.basicConfig(level=logging.INFO)

    # dp.update.middleware(middleware)
    dp.message.middleware(middlewares.CancelMiddleware())
    dp.include_routers(
        admin.router,
        payments.router,
        user.router,
    )
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
