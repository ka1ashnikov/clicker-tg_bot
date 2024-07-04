from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

go_webapp = ReplyKeyboardMarkup(
    keyboard=
    [
            [
                KeyboardButton(text='Go webapp', web_app= WebAppInfo(url='https://ka1ashnikov.github.io/clicker-tg_bot/webapp/'))
            ]
    ]
, resize_keyboard=True) 


