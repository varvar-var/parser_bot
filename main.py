import telebot
from telebot import types
from hbr import get_articles
from dotenv import load_dotenv
import os


load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

flows = {'Фронтенд' : 'https://habr.com/ru/flows/frontend/articles/', 
        'Бэкенд' : 'https://habr.com/ru/flows/backend/articles/',
        'Научпоп' : 'https://habr.com/ru/flows/popsci/articles/',
        'Дизайн' : 'https://habr.com/ru/flows/design/articles/',
        'Менеджмент' : 'https://habr.com/ru/flows/management/articles/',
        'Новое': 'https://habr.com/ru/feed/'}

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! 👋', reply_markup=keyboard())

def keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = []
    for i in flows:
        btn = types.KeyboardButton(i)
        buttons.append(btn)
    markup.add(*buttons)    
    return markup

@bot.message_handler(func=lambda message: True)  
def handle_all(message):
    if message.text in flows:
        articles = get_articles(flows[message.text])
        for title, link in articles.items():
            bot.send_message(message.chat.id, f'{title}\n\n{link}')        
    else:                                    
        bot.send_message(message.chat.id,'Я вас не понял')               

if __name__ == '__main__':
    bot.polling(non_stop=True)    