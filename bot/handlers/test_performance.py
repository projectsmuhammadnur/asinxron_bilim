import json
import random

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from bot.buttons.inline_buttons import science_menu_button, topics_menu_button, test_performance_menu_button
from bot.buttons.reply_buttons import main_menu_buttons
from bot.buttons.text import performance
from bot.dispatcher import dp


def get_test(topic_id: int):
    tests = json.loads(requests.get(url=f'http://127.0.0.1:8000/tests/filter/{topic_id}/').content)['results']
    num = random.randint(1, len(tests))
    num = tests[num - 1]['id']
    return json.loads(requests.get(url=f'http://127.0.0.1:8000/tests/detail/{num}/').content)


@dp.message_handler(Text(performance))
async def get_science_function(msg: types.Message):
    session = await msg.answer(text=f"⏳", reply_markup=ReplyKeyboardRemove())
    await session.delete()
    await msg.answer(text="Fanni tanlang 📚", reply_markup=await science_menu_button())


@dp.callback_query_handler(Text(startswith='science_'))
async def get_topic_function(call: types.CallbackQuery):
    data = call.data.split('_')[-1]
    await call.message.delete()
    await call.message.answer(text="Mavzuni tanlang 📖", reply_markup=await topics_menu_button(data))


@dp.callback_query_handler(Text(startswith='topic_'))
async def get_performance_function(call: types.CallbackQuery, state: FSMContext):
    data = call.data.split('_')[-1]
    async with state.proxy() as state_data:
        state_data['topic_id'] = data
    test = get_test(data)
    await state.set_state('test_performance')
    await call.message.delete()
    await call.message.answer(text=f"""
📑 Shart: {test['description']}
❓ Savol: {test['question']}

A: {test['a']}
B: {test['b']}
C: {test['c']}
D: {test['d']}
""", reply_markup=await test_performance_menu_button(test))


@dp.callback_query_handler(Text(startswith='answer_'), state="test_performance")
async def test_performance_function(call: types.CallbackQuery, state: FSMContext):
    txt, test_id, status = call.data.split('_')
    user = json.loads(requests.get(url=f"http://127.0.0.1:8000/telegram-users/chat_id/{call.from_user.id}/").content)
    step_data = user['step']
    step_data.update({test_id: status})
    requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/",
                   data={'step': json.dumps(step_data)})
    async with state.proxy() as data:
        pass
    tests = json.loads(requests.get(url=f'http://127.0.0.1:8000/tests/filter/{data["topic_id"]}/').content)['results']
    if len(tests) == len(step_data):
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

Tabriklaymiz bu mavzudagi barcha testni tugatdingiz 🥳
""", reply_markup=await main_menu_buttons())
        await state.finish()
        requests.patch(url=f"http://127.0.0.1:8000/telegram-users/update/{user['id']}/", data={'step': json.dumps({})})
    else:
        k = True
        while k:
            test = get_test(data['topic_id'])
            s_data = step_data.get(str(test['id']))
            if s_data is None:
                k = False
        await call.message.delete()
        r = "noto'g'ri ❌"
        if status == 'true':
            r = "to'g'ri ✅"
        await call.message.answer(text=f"""
Javobingiz {r}        

📑 Shart: {test['description']}
❓ Savol: {test['question']}

A: {test['a']}
B: {test['b']}
C: {test['c']}
D: {test['d']}
    """, reply_markup=await test_performance_menu_button(test))
