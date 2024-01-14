import telebot
import datetime
from telebot import types

bot = telebot.TeleBot('6972907021:AAGvTbmTXt1jOzHjmSgM0re5PIYt5tVYOxE')

@bot.message_handler(commands=['start'])
def started(message):
    markup = types.InlineKeyboardMarkup()
    b3 = types.InlineKeyboardButton('Помощь с ботом', callback_data='hel')
    b4 = types.InlineKeyboardButton('Главное о боте', callback_data='mai')
    b5 = types.InlineKeyboardButton('Информация о вас', callback_data='inf')
    b6 = types.InlineKeyboardButton('Открыть мессенджер', callback_data='channe')
    markup.row(b3, b4)
    markup.row(b5, b6)
    bot.send_message(message.chat.id, '<b>Привет!</b> Это мой первый бот! Выбери команду, которая тебе нужна:\n\n'
                                      'Ты можешь поздороваться с ботом, введя "Привет" или получить свой id, введя "id"', parse_mode='html', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "hel":
        helper(call.message)
    elif call.data == "mai":
        mainer(call.message)
    elif call.data == "inf":
        infos(call.message)
    elif call.data == "channe":
        site(call.message)
    elif call.data == "auth":
        authors(call.message)
    elif call.data == "day":
        dater(call.message)

def helper(message):
    markup = types.InlineKeyboardMarkup()
    b7 = types.InlineKeyboardButton('Информация об авторе', callback_data='auth')
    b8 = types.InlineKeyboardButton('Текущая дата', callback_data='day')
    markup.row(b7, b8)
    bot.send_message(message.chat.id, '<b>Какая помощь тебе нужна?</b> (выбери из предложенного)\n\n', reply_markup=markup, parse_mode='html')

def authors(message):
    bot.send_message(message.chat.id, 'Диана')

def site(message):
    markup = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton('Ютуб', url='https://www.youtube.com')
    markup.row(b1)
    b2 = types.InlineKeyboardButton('ВК', url='https://vk.com')
    b3 = types.InlineKeyboardButton('ОК', url='https://ok.ru')
    markup.row(b2, b3)
    bot.send_message(message.chat.id, "Нажмите на кнопку с нужным сайтом:", reply_markup=markup)

def dater(message):
    bot.send_message(message.chat.id, f'Сегодня: {datetime.date.today()}')

def mainer(message):
    bot.send_message(message.chat.id, 'Это мой первый бот!')

def infos(message):
    if message.from_user.last_name is None:
        info_text = f'Тебя зовут: {message.from_user.first_name}\nТвоя фамилия: Не указано в профиле'
    else:
        info_text = f'Тебя зовут: {message.from_user.first_name}\nТвоя фамилия: {message.from_user.last_name}'
    bot.send_message(message.chat.id, f'<b>Информация о вас:</b>\n{info_text}', parse_mode='html')

@bot.message_handler(func=lambda message: True)
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    elif message.text.lower() == 'id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}')

bot.polling(none_stop=True)
