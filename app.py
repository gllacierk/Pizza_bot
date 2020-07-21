from loader import bot
from keyboards.reply import main_keyboard
from data import admin_id


async def on_startup(dp):
    await bot.send_message(chat_id=admin_id, text="start_poling", reply_markup=main_keyboard)


async def on_shutdown(dp):
    pass


if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
