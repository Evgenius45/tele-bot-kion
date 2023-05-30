import re

from loader import bot
from states.st_custom import St_custom
from utils.misc.git_kinopoisk_api import kinopisk_api


@bot.message_handler(commands=['custom'])
def start_ex(message):
    """
    Запрос диапазона поиска по годам.
    """

    bot.set_state(message.from_user.id, St_custom.year_custom, message.chat.id)
    bot.send_message(message.chat.id, 'Фильмы какого года выпуска\nхотите найти (пр. 2000-2005)')


@bot.message_handler(state=St_custom.year_custom)
def ask_age(message):
    """
    Запрос диапазона поиска рейтинга.
    """

    if re.match('\d{4}-\d{4}$', message.text):
        bot.send_message(message.chat.id, "Введите нужный диапазон\nрейтинга (от 0 до 10, пр. 1-8)")
        bot.set_state(message.from_user.id, St_custom.rating_custom, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['year'] = message.text

    else:
        bot.send_message(message.chat.id, "Вы ввели не правильный формат даты")


@bot.message_handler(state=St_custom.rating_custom)
def ready_for_answer(message):
    """
    Вывод результатов и запрос данных c API
    """

    if re.match('^[0-9]{1}-([0-9]{1}$|10$)', message.text):
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            table = data

        response = kinopisk_api(table['year'], message.text, -1)

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
