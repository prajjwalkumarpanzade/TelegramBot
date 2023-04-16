import os
import telebot
from dotenv import load_dotenv
from app.openai_api.openai_chat import ai_response

load_dotenv()

telebot_token = os.getenv('TELEBOT_TOKEN')

bot = telebot.TeleBot(token=telebot_token,parse_mode=None)

@bot.message_handler(commands=['ai'])
def ai_handler(message):
    if message.text == '/ai':
        bot.reply_to(message,'Please enter what you want.')

    
    else:
        
        refine_message = message.text.replace('/ai','') 
        
        if (refine_message.startswith('??') and 'program' in refine_message) or (refine_message.startswith('??') and 'code' in refine_message) :
            response = f"""
            
            {ai_response(refine_message)}
            """
            
            bot.reply_to(message,response)


        if 'program' in refine_message or 'code' in refine_message:
            refine_message += 'give algorithm not code'
            response = f"""
            {ai_response(refine_message)}
            """
            bot.reply_to(message,response)
            # print(refine_message)
            # print(len(refine_message))

    

        else:
            # refine_message = message.text.replace('/ai','')
            response = f"""
            
            {ai_response(refine_message)}
            """
            
            bot.reply_to(message,response)