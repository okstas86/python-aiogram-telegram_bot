from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


#  кнопки клаавиатуры админа

button_load= KeyboardButton('/загрузить')
button_delete= KeyboardButton('/удалить')

button_case_admim = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete)

