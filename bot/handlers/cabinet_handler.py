import json

import requests
from aiogram import types
from aiogram.dispatcher.filters import Text

from bot.buttons.text import cabinet
from bot.dispatcher import dp


@dp.message_handler(Text(cabinet))
async def get_science_function(msg: types.Message):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    await msg.answer(text=f"""
🧾 Ismingiz: {user['name']}
🆔 ID: {user['chat_id']}
🪙 Coin: 0
""")
