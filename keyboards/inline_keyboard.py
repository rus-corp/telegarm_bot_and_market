from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = InlineKeyboardMarkup(row_width=1)
catalog_btn = InlineKeyboardButton(text='Каталог', callback_data='catalog')


catalog_menu = InlineKeyboardMarkup(row_width=2)
kotels_btn = InlineKeyboardButton(text='котлы', callback_data='kotels')
gas_heater_btn = InlineKeyboardButton(text='Газовые колонки', callback_data='gas_heater')

choise_power = InlineKeyboardMarkup(row_width=2)
power_btn1 = InlineKeyboardButton(text='10л', callback_data='10l')
power_btn2 = InlineKeyboardButton(text='12л', callback_data='12l')
power_btn3 = InlineKeyboardButton(text='14л', callback_data='14l')
power_btn4 = InlineKeyboardButton(text='16л', callback_data='16l')

price_diapozon = InlineKeyboardMarkup(row_width=1)
price_diap_btn1 = InlineKeyboardButton(text='50 000 - 55 000', callback_data='50t')
price_diap_btn2 = InlineKeyboardButton(text='55 000 - 60 000', callback_data='55t')
price_diap_btn3 = InlineKeyboardButton(text='60 000 - 70 000', callback_data='70000')

choise_power.add(power_btn1, power_btn2, power_btn3, power_btn4)
main_menu.add(catalog_btn)
catalog_menu.add(kotels_btn, gas_heater_btn)
price_diapozon.add(price_diap_btn1, price_diap_btn2, price_diap_btn3)

