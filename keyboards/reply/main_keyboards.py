from aiogram import types

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu_button = types.KeyboardButton(text="Заказать еду 🍴")
cart_button = types.KeyboardButton(text="Корзина 👜")
help_button = types.KeyboardButton(text="Помощь ❓")

main_keyboard.add(menu_button)
main_keyboard.add(cart_button, help_button)
