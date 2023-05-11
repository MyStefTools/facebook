
import os, sys
import requests

try:

	import telebot

	import time, base64, marshal, zlib, py_compile

except:

	os.system('pip install telebot')

	os.system('pip install Pytelegrambotapi==3.7.7')

	os.system('pip install time')

	os.system('pip install base64')

	os.system('pip install marshal')

	os.system('pip install zlib')

	os.system('pip install py_compile')

	

token = "6161707123:AAF2A447yKIfpCoA8oE8eY3xGRn4_B4-VkM"

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['greet','start'])

def start(message):

 

 bot.send_message(message.chat.id, f"""<strong>الان ارسل ملف بايثون ليتم التشفير  

ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

• مميزات التشفير الذي تشفره

• يتم الحمايه بأكثر من طبقه

ـ marshal,base46,zlib ـ

 ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ

 معرفي @V_S_Y </strong>""",parse_mode="html")

 @bot.message_handler(content_types=['document'])

 def send(message):

 	 bot.get_file(message.document.file_id)

 	 #bot.download_file(file_info.file_path)

 	# bot.send_photo(message.chat.id,open("file","rb"))

 	 file_info = bot.get_file(message.document.file_id)

 	 use = bot.download_file(file_info.file_path)

 	 bot.send_message(message.chat.id, f"""<strong> ⏱️ Wait a little please …</strong>""",parse_mode="html")

 	 cv =str("# CODE BY : MOUAD › \n# Tele : @V_S_Y")

 	 sa = compile(use, 'dg', 'exec')

 	 sb = marshal.dumps(sa)

 	 sc = zlib.compress(sb)

 	 sd = base64.b85encode(sc)

 	 b = '#https://t.me/V_S_Y\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b85decode(' + repr(sd) + '))))'

 	 d = open('Cncryption_mouad.py', 'w')

 	 d.write(b+'\n'+cv)

 	 d.close()

 	 file = {'document':open('Cncryption_mouad.py','rb')}

 	 tex = ("✅ Done Encryption File 🥀.")

 	 requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={message.chat.id}&caption={tex}', files=file)

 	 #bot.send_message(message.chat.id, f"""<strong> ✅ Done Encryption File 🥀. </strong>""",parse_mode="html")

 	 os.system(f'rm -rf Cncryption_mouad.py')

  	

bot.polling(True)
