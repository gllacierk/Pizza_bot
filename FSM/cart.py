from aiogram.dispatcher.filters.state import StatesGroup, State


class Cart(StatesGroup):
    InCart = State()
    DoOrder = State()
