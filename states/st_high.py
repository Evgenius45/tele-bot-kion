from telebot.handler_backends import State, StatesGroup


class St_high(StatesGroup):
    year_high = State()
    rating_high = State()
