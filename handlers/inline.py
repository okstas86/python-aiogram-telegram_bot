from aiogram import types
from create_bot import dp
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# кнопка ссылка
urlkb = InlineKeyboardMarkup(row_width=2)
urlbutton = InlineKeyboardButton( text='Instagram',url='https://www.instagram.com/pepperhotmsk/')
urlbutton2=InlineKeyboardButton(text='Видио', url= 'https://m.youtube.com/watch?v=O81G1fw4y-M&feature=youtu.be' )
x=[
    InlineKeyboardButton(text='ссылка_3', url= 'https://www.google.com/'),
    InlineKeyboardButton(text='ссылка_4',url= 'https://www.google.com/'),
    InlineKeyboardButton(text='ссылка_3',url= 'https://www.google.com/'),
   ]
urlkb.add(urlbutton,urlbutton2).row(*x)

@dp.message_handler(commands='ссылки')
async def url_command(message:types.Message):
    await message.answer('cсылки: ', reply_markup=urlkb)




