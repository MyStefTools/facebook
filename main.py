import requests
import telebot
from uuid import uuid4
from user_agent import generate_user_agent
from telebot import types
token = "6241047580:AAF0QQn49Bxf17s75wovJ_6dm8Nkx7aVod8"
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['greet','start'])
def start(message):
 
 bot.send_message(message.chat.id, f"- Hi Send Id to check out\n- مرحبا ارسل الايدي لفحصه\nDevelopers : @QFFFFFQ\nمطوري : @QFFFFFQ")
 @bot.message_handler(func=lambda followinG:True )

 def re(message):
     use =(message.text)
     id=f'{use}'
     SS=requests.get(f'http://instaup.marsapi.com/get_likes/shop/daily_coins?user_id={id}').text
     if '"coins":"' in SS :
     	co = str(SS.split('"coins":"')[1])
     	coinx=str(co.split('"')[0])
     	coin=int(coinx)
     	don=f'''- Hi Done Get Coin ✅ 
— — — — — — — — — — — — — —
- Id : {id}
- Coin : {coin}
— — — — — — — — — — — — — —
- By : @QFFFFFQ - @GGGeG7'''
     	bot.send_message(message.chat.id, f"{don}")
     else:
     		hh =f"""
- Error Id
- By: @QFFFFFQ"""
     		bot.send_message(message.chat.id, f"{hh}")


bot.polling(True)
