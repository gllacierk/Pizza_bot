from aiogram import types

menu_keyboard = types.InlineKeyboardMarkup(row_width=1)
pizza_button = types.InlineKeyboardButton(text="Пицца 🍕", callback_data="pizza")
sushi_button = types.InlineKeyboardButton(text="Суши и роллы 🍣", callback_data="sushi")
burger_button = types.InlineKeyboardButton(text="Гамбургеры 🍔", callback_data="burger")
drink_button = types.InlineKeyboardButton(text="Напитки 🥤", callback_data="drink")

menu_keyboard.add(pizza_button, sushi_button, burger_button, drink_button)
