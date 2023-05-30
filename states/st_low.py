from telebot.handler_backends import State, StatesGroup


class St_low(StatesGroup):
    year = State()
    rating = State()
