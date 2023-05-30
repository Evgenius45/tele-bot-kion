from telebot.types import Message

from database.common.models import db, History
from database.core import inter_db
from loader import bot


@bot.message_handler(commands=['history'])
def bot_help(message: Message):
    print('dfdfdfdfff')
    retrieve = inter_db.retrieve()
    result = retrieve(db, History, History.yars, History.rat_kp, History.sort)
    text = [f'Год: {i_history.yars}, Рейтинг: {i_history.rat_kp}, Сортировка: {i_history.sort}' for i_history in result[-10:]]
    bot.reply_to(message, '\n'.join(text))
