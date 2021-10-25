import telebot
import requests
import json
import time

bot = telebot.TeleBot("<your-api-key>")
@bot.message_handler(commands=['wrxinr', 'shibinr'])
def send_welcome(message):
	global origwrx
	global origshib
	b = (message.text).split()
	if b[0] == '/wrxinr':
		try:
			temporigwrx = float(b[1])
			m = json.load(open('data.json'))
			m["origwrx"] = temporigwrx
			a_file = open("data.json", "w")
			json.dump(m, a_file)
			a_file.close()
			bot.reply_to(message, f"Successfully Updated Price new price {temporigwrx}")
		except:
			bot.reply_to(message, "something wrong")
	if b[0] == '/shibinr':
		try:
			temporigshib = float(b[1])
			m = json.load(open('data.json'))
			m["origshib"] = temporigshib 
			a_file = open("data.json", "w")
			json.dump(m, a_file)
			a_file.close()
			bot.reply_to(message, f"Successfully Updated Price new price {origshib}")
		except:
			bot.reply_to(message, "something wrong")
bot.infinity_polling()
