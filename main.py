import time,random
import requests
import telebot
from telebot import types

token = "5999438570:AAEy1Ul--yB3J6ll9RHAH4Fx7znxSN3YiVk"
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def start(message):
	topac = types.InlineKeyboardMarkup()
	top = types.InlineKeyboardButton("- Dev", url = "t.me/qfffffq")
	topac.add(top)
	idph = f"https://t.me/{message.from_user.username}"
	bot.send_photo(message.chat.id,idph,'''- Hello your in Bot Get Info TikTok Send Username .\n- مرحبا بك في بوت جلب معلومات تيك توك ارسل يوزرك لكشف معلوماته''', parse_mode="markdown",reply_markup=topac)
	
	@bot.message_handler(func=lambda followinG:True )
	
	def com(message):
		username = str(message.text)
		url = f"https://tiktok-best-experience.p.rapidapi.com/user/{username}"
		he = {
  "x-rapidapi-key":"d0cbbe1f79mshe3c74080d9d0da5p1de4ddjsn21db44140e77",
  "x-rapidapi-host":"tiktok-best-experience.p.rapidapi.com",
  "User-Agent":"TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 14.4.0) Alamofire/5.4.4"
         		}
		res = requests.get(url=url, headers=he).json()
		try:
         			followers=res['data']['follower_count']
         			name=res['data']['nickname']
         			tlg = f'''———————×———————
𝑵𝑨𝑴𝑬 : {name}
𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬 : {username}
𝑬𝑴𝑨𝑰𝑳 : {username}@gmail.com
𝑭𝑶𝑳𝑳𝑶𝑾𝑬𝑹𝑺 : {followers}
𝑼𝑹𝑳 : https://www.tiktok.com/@{username}
———————×———————
𝑷𝑹𝑶𝑮𝑹𝑨𝑴𝑴𝑬𝑹 : @QFFFFFQ
𝑴𝒀 𝑪𝑯𝑨𝑵𝑵𝑬𝑳 : @GGGeG7'''
         			top = types.InlineKeyboardButton("- Dev", url = "t.me/qfffffq")
         			to = types.InlineKeyboardButton("- voice", url = url)
         			topac.add(top,to)
         			bot.send_message(message.chat.id,f'{tlg}',)
		except:
			         			tt = f'''- Error User '''
			         			top = types.InlineKeyboardButton("- Dev", url = "t.me/QFFFFFQ")
			         			bot.send_message(message.chat.id,f'{tt}',)
bot.polling(True)