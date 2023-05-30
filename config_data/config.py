import os

from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
KINOPOISK_DEV_TOKEN = os.getenv('KINOPOISK_DEV_TOKEN')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести  справку"),
    ('low', "Фильмы с минимальным рейтингом"),
    ('high', "Фильмы с максимальным рейтингом"),
    ('custom', "Пользовательский диапазон рейтинга"),
    ('history', "История запросов пользователей"),
)
