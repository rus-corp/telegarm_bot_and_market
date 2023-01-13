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

