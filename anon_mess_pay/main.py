import asyncio
from aiogram import Bot, Dispatcher
from data import config
from data.database.db import check_db
from app import register_all_routers
from data.config import logger, token, update_bot_info


async def main():
    db_connection = check_db()
    config.init_settings()
    bot = Bot(token=token)
    bot_info = await bot.get_me()
    update_bot_info(bot_info)
    dp = Dispatcher()
    register_all_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logger.info("Bot started")
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped")
        print('Exit')
