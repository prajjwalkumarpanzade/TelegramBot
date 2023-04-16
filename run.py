import time
from app.telebot import bot
import alive 


if __name__=='__main__':
    
    alive.keep_alive()
    print('Bot is running...')
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
    # bot.infinity_polling()
