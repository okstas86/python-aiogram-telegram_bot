from aiogram.utils import executor
from create_bot import dp
from handlers import client,admin,other,inline
from data_base import sqlite_db







async def on_startup(_):
    print('Bot online!')
    sqlite_db.sql_start()

client.register_handler_client(dp)
admin.register_handler_admin(dp)
other.register_handler_other(dp)







    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

client.register_handler_client(dp)
other.register_handler_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)