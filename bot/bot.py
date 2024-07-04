from aiogram import F, types
from aiogram.types import ReplyKeyboardMarkup
from aiogram.filters import Command
from aiogram import Router

import markups


router = Router()


@router.message(Command('menu', 'start'))
async def welcome(message: types.Message):
    await message.answer('Hello', reply_markup = markups.go_webapp)


