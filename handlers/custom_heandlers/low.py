import re

from utils.misc.git_kinopoisk_api import kinopisk_api
from states.st_high import St_high
from loader import bot


@bot.message_handler(commands=['low'])
def start_ex(message):
    """
    Запрос диапазона поиска по годам.
    """

    bot.set_state(message.from_user.id, St_high.year_high, message.chat.id)
    bot.send_message(message.chat.id, 'Фильмы какого года выпуска\nхотите найти (пр. 2000-2005)')


@bot.message_handler(state=St_high.year_high)
def ask_age(message):
    """
    Запрос минимального рейтинга.
    """

    if re.match('\d{4}-\d{4}$', message.text):
        bot.send_message(message.chat.id, "Введите минимальный рейтинг(от 0 до 9)")
        bot.set_state(message.from_user.id, St_high.rating_high, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['year'] = message.text

    else:
        bot.send_message(message.chat.id, "Вы ввели не правильный формат даты")


@bot.message_handler(state=St_high.rating_high)
def ready_for_answer(message):
    """
    Вывод результатов и запрос данных c API
    """

    if re.match('^[0-9]$', message.text):
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            table = data

        interval_rating = f'{message.text}'+'-10'
        response = kinopisk_api(table['year'], interval_rating)

        if len(response) == 0:
            bot.send_message(message.chat.id, 'Поиск не дал результатов.')
            bot.delete_state(message.from_user.id, message.chat.id)

        else:
            for text in response:
                msg = (f'<b>{text["name"]}</b>\n'
                       f'Год выпуска: {text["year"]}\n'
                       f'Рейтинг KP: {text["rating"]}\n')

                bot.send_photo(message.chat.id, photo=text["poster"], caption=msg, parse_mode="html")
                bot.delete_state(message.from_user.id, message.chat.id)

    else:
        bot.send_message(message.chat.id, "Вы ввели не правильный формат рейтинга")
