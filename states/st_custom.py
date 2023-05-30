from telebot.handler_backends import State, StatesGroup


class St_custom(StatesGroup):
    year_custom = State()
    rating_custom = State()
