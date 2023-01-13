from aiogram.dispatcher.filters import Command
from aiogram import types
from aiogram.types import Message, CallbackQuery
from main import dp
from keyboards.inline_keyboard import main_menu, catalog_menu, choise_power, price_diapozon
import time
from vodyanoy_db.db_query import get_gas_heater
from main import bot



@dp.message_handler(Command('start'))
async def show_menu(message: Message):
    await message.answer(f'Здравствуйте {message.from_user.first_name}, добро пожаловать к нам в магазин! Взягляните на наш каталог', reply_markup=main_menu)

@dp.callback_query_handler(text='catalog')
async def catalog_coma(message: types.Message):
    await bot.send_message(message.from_user.id, 'Отлично', reply_markup=catalog_menu)

@dp.callback_query_handler(text_contains='gas_heater')
async def kotels_comand(call: CallbackQuery):
    await call.message.answer(text='Теперь выберете мощность:', reply_markup=choise_power)
    name = call.data

@dp.callback_query_handler(text_contains='10l')
async def power_choise_10l(call:CallbackQuery):
    await call.message.answer(text='Какой ценовой диапозон выберите?:', reply_markup=price_diapozon)

@dp.callback_query_handler(text_contains='70000')
async def show_variant(call:CallbackQuery):
    price = call.data
    print(price)
    result = get_gas_heater(price)
    await call.message.answer(result)







    