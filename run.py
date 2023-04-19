from app.telebot import bot
from app.alive import keep_alive

if __name__=='__main__':
    keep_alive()
    print('Bot is running...')
    bot.infinity_polling(none_stop=True)