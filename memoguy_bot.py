from cgitb import text
from email.mime import image
import telebot
import urllib

bot = telebot.TeleBot('EnterToken')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Пупа или лупа...')

@bot.message_handler(content_types=["text"])
def handle_text (message):
    if message.text == "Пупа":
        bot.send_message(message.chat.id, message.text + ' и что?')
    elif message.text == "Лупа":
        url='https://img.randme.me'
        chat_id=message.chat.id
        msgid=message.message_id
        f = open('mem.jpg','wb')
        req=urllib.request.Request(url,data=None,headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'})
        f.write(urllib.request.urlopen(req).read())
        f.close()
        img=open('mem.jpg', 'rb')
        bot.send_photo(chat_id, img , reply_to_message_id=msgid)
    else:
        bot.send_message(message.chat.id, 'на нет и суда нет')



# @bot.message_handler(content_types=["text"])
# def handle_photo(message):
#     chat_id=message.chat.id
#     msgid=message.message_id
#     img=open('mem.jpg', 'rb')
#     bot.send_photo(chat_id, img , reply_to_message_id=msgid)


bot.polling(none_stop=True, interval=0)