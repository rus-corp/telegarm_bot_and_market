from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = InlineKeyboardMarkup(row_width=1)
catalog_btn = InlineKeyboardButton(text='Каталог', callback_data='catalog')

catalog_menu = InlineKeyboardMarkup(row_width=2)
kotels_btn = InlineKeyboardButton(text='котлы', callback_data='kotels')
gas_heater_btn = InlineKeyboardButton(text='Газовые колонки', callback_data='gas_heater')


main_menu.add(catalog_btn)
catalog_menu.add(kotels_btn, gas_heater_btn)


