from loader import dp
from aiogram.types import Message


@dp.message_handler(text="pizza")
async def pizza_handler(message: Message):
    await message.answer(text="Меню пиццы", reply_markup=pizza_menu)