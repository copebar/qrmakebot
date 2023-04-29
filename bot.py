import telebot
import qrcode
import os

bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Приветствую тебя в боте для создания QR кодов. Для создания QR кода используйте команду /makeqr')
	
@bot.message_handler(commands=['makeqr'])
def makeqr(message):
	mess = bot.send_message(message.chat.id, 'Отправьте ссылку или текст который должен содержаться в QR коде')
	bot.register_next_step_handler(mess, makeqrcode)
	
def makeqrcode(message):
	img = qrcode.make(message.text)
	try:
		img.save(f'{message.chat.id}.png')
		bot.send_photo(message.chat.id, photo=open(f'{message.chat.id}.png', 'rb'))
		os.remove(f'{message.chat.id}.png')
	except:
		bot.send_message(message.chat.id, 'Произошла ошибка, попробуйте ещё раз')
		
@bot.message_handler(content_types=['text'])
def text(message):
	bot.send_message(message.chat.id, 'Неизвестная команда! Для создания QR кода используйте команду /makeqr')

bot.polling(none_stop=True)