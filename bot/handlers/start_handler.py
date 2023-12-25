import json
import uuid

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text

from bot.buttons.reply_buttons import main_menu_buttons
from bot.buttons.text import back_main_menu
from bot.dispatcher import dp, bot
from main import admins


@dp.message_handler(Text(back_main_menu))
async def back_main_menu_function_1(msg: types.Message):
    await msg.answer(text=f"Asosiy menu🏠", reply_markup=await main_menu_buttons())


@dp.callback_query_handler(Text(back_main_menu))
async def back_main_menu_function_2(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text=f"Asosiy menu🏠", reply_markup=await main_menu_buttons())


@dp.callback_query_handler(Text(back_main_menu), state="test_performance")
async def back_main_menu_function_3(call: types.CallbackQuery, state: FSMContext):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
    t, f = 0, 0
    for k, v in user['step'].items():
        if v == "true":
            t += 1
        else:
            f += 1
    await call.message.delete()
    await call.message.answer(text=f"""
{len(user['step'])} ta test 📝
{t} ta to'g'ri ✅
{f} ta noto'g'ri ❎
""", reply_markup=await main_menu_buttons())
    await state.finish()
    requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data={'step': json.dumps({})})


@dp.message_handler(CommandStart())
async def start_handler(msg: types.Message, state: FSMContext):
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    try:
        if user['detail']:
            await state.set_state("set_name")
            await msg.answer(text="✏️ Ism-Familiyangizni yuboring")
            data = {
                "chat_id": str(msg.from_user.id),
                "username": msg.from_user.username,
                "full_name": msg.from_user.full_name,
                "step": json.dumps({})
            }
            requests.post(url=f"http://127.0.0.1:8000/telegram-users/create/", data=data)
            for admin in admins:
                await bot.send_message(chat_id=admin, text=f"""
Yangi user🆕
ID: <a href='tg://user?id={msg.from_user.id}'>{msg.from_user.id}</a>
Ism-Familiya: {msg.from_user.full_name}
Username: @{msg.from_user.username}\n""", parse_mode='HTML')
    except KeyError:
        await msg.answer(text="Bot yangilandi ♻️", reply_markup=await main_menu_buttons())


@dp.message_handler(state='set_name')
async def set_name_function(msg: types.Message, state: FSMContext):
    await msg.answer(text="Xush kelibsiz 🌐", reply_markup=await main_menu_buttons())
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{msg.from_user.id}/").content)
    data = {"name": msg.text}
    requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data=data)
    await state.finish()
