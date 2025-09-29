import asyncio
import logging
from logging import basicConfig
from aiogram import Bot, Dispatcher,F
from config.config import Config , load_config
from handlers import other , user

async def start_bot() ->None:
    config:Config = load_config()

    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format
    )

    bot = Bot(token=config.bot.token)
    dp = Dispatcher()
    #Рег роутеры в диспетчер
    dp.include_router(user.router)
    dp.include_router(other.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(start_bot())