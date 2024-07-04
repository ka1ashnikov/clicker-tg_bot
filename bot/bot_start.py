import os
import sys
import asyncio
import logging

from aiogram import Bot, Dispatcher 
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import load_dotenv
from datetime import datetime

from bot import router


dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))


def onBot_startup():
    curr_time = datetime.now()
    print(f'Started at {curr_time}.')


async def main():
    await dp.start_polling(bot, on_startup=onBot_startup())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
