from loader import dp
from aiogram.types import Message
from keyboards.reply import main_keyboard
from aiogram import types


@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    await message.answer(text="Главное меню", reply_markup=main_keyboard)


@dp.message_handler(commands=["help"])
async def help_command(message: Message):
    await message.answer(text="help_text", reply_markup=main_keyboard)