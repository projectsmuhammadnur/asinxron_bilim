import json

import requests
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.buttons.text import back_main_menu, end_test


async def science_menu_button():
    sciences = json.loads(requests.get(url=f"http://127.0.0.1:8000/sciences/").content)['results']
    keyboard = InlineKeyboardMarkup(row_width=3)
    for science in sciences:
        button = InlineKeyboardButton(text=science['name'], callback_data=f"science_{science['id']}")
        keyboard.add(button)
    keyboard.add(InlineKeyboardButton(text=back_main_menu, callback_data=back_main_menu))
    return keyboard


async def topics_menu_button(science_id):
    topics = json.loads(requests.get(url=f"http://127.0.0.1:8000/topics/filter/{science_id}/").content)['results']
    keyboard = InlineKeyboardMarkup(row_width=3)
    for topic in topics:
        button = InlineKeyboardButton(text=topic['name'], callback_data=f"topic_{topic['id']}")
        keyboard.add(button)
    keyboard.add(InlineKeyboardButton(text=back_main_menu, callback_data=back_main_menu))
    return keyboard


async def test_performance_menu_button(test: dict):
    design = []
    if test['correct_answer'] == 'a':
        design.append([InlineKeyboardButton(text="A", callback_data=f'answer_{test["id"]}_true')])
        design.append([InlineKeyboardButton(text="B", callback_data=f'answer_{test["id"]}_false')])
        design.append([InlineKeyboardButton(text="C", callback_data=f'answer_{test["id"]}_false')])
        design.append([InlineKeyboardButton(text="D", callback_data=f'answer_{test["id"]}_false')])
    elif test['correct_answer'] == 'b':
        design.append([InlineKeyboardButton(text="A", callback_data=f'answer_{test["id"]}_false')])
        design.append([InlineKeyboardButton(text="B", callback_data=f'answer_{test["id"]}_true')])
        design.append([InlineKeyboardButton(text="C", callback_data=f'answer_{test["id"]}_false')])
        design.append([InlineKeyboardButton(text="D", callback_data=f'answer_{test["id"]}_false')])
    elif test['correct_answer'] == 'c':
        design.append([InlineKeyboardButton(text="A", callback_data=f'answer_{test["id"]}_false')])
        design.append([InlineKeyboardButton(text="B", callback_data=f'answer_{test["id"]}_false')])
        design.append([InlineKeyboardButton(text="C", callback_data=f'answer_{test["id"]}_true')])
        design.append([InlineKeyboardButton(text="D", callback_data=f'answer_{test["id"]}_false')])
    else:
        design.append([InlineKeyboardButton(text="A", callback_data=f'answer_{test["id"]}_false')])
        design.append([InlineKeyboardButton(text="B", callback_data=f'answer_{test["id"]}_false')])
        design.append([InlineKeyboardButton(text="C", callback_data=f'answer_{test["id"]}_false')])
        design.append([InlineKeyboardButton(text="D", callback_data=f'answer_{test["id"]}_true')])
    design.append([InlineKeyboardButton(text=end_test, callback_data=end_test)])
    return InlineKeyboardMarkup(inline_keyboard=design)
