import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
import keyboards as kv
from aiogram.types import callback_query

import os
from config import token

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(text='/start')
async def start_command(message: types.Message):
    await message.answer(f'Здравствуйте {message.from_user.first_name}, добро пожаловать к нам в магазин!')
    time.sleep(0.2)
    await bot.send_message(message.from_user.id, 'Взягляните на наш каталог', reply_markup=kv.main_menu)


# @dp.callback_query_handler(text='catalog')
# async def catalog_coma(callback: types.CallbackQuery):
#     await callback.message.edit_reply_markup('Отлично', reply_markup=)


# @dp.callback_query_handler(text='каталог')
# async def catalog_coma(callback: types.CallbackQuery):
#     await callback.message.edit_reply_markup(reply_markup=product_ikb)

# @dp.message_handler(text='catalog')
# async def catalog_command(message: types.Message):
#     await message.answer('Взгляните на наши товары:', reply_markup=prod1, prod2)
    



# @dp.message_handler(commands=['start'])
# async def start_message(message: types.Message):
#     await message.answer('Каталог', reply_markup=inkb)










executor.start_polling(dp, skip_updates=True)

