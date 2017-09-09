import telepot
bot = telepot.Bot('401378315:AAG6qBm1DH5TmgfrdD-WNfVGka0VA5RNgtk')

import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

token = '401378315:AAG6qBm1DH5TmgfrdD-WNfVGka0VA5RNgtk'
URL = 'https://api.telegram.org/bot401378315:AAG6qBm1DH5TmgfrdD-WNfVGka0VA5RNgtk/getUpdates'

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Next Lesson', callback_data='press')],
                   [InlineKeyboardButton(text='Timetable',callback_data='press')],
                   [InlineKeyboardButton(text='Setting',callback_data='press')],
               ])

    bot.sendMessage(chat_id, 'Hello master. What can I do for you?', reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')

TOKEN = '401378315:AAG6qBm1DH5TmgfrdD-WNfVGka0VA5RNgtk'  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
