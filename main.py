import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import main_table, blinking, dormitories, admin_panel, announcement, helpers, utils


async def main():
    load_dotenv()
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(helpers.router, announcement.router, admin_panel.router, blinking.router, dormitories.router,
                       main_table.router, utils.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
