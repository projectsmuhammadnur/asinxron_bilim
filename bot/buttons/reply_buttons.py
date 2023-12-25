import json

import requests
from aiogram.types import ReplyKeyboardMarkup

from bot.buttons.text import back_main_menu, adverts, none_advert, forward_advert, performance


async def main_menu_buttons():
    design = [
        [performance]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def back_main_menu_button():
    design = [[back_main_menu]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def admin_menu_buttons():
    design = [
        [adverts],
        [back_main_menu]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


async def advert_menu_buttons():
    design = [
        [none_advert, forward_advert],
        [back_main_menu]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
