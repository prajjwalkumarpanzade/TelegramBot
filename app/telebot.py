from dotenv import load_dotenv
from string import punctuation
from .openai_chat import generate_response
import telebot
import os
import time

load_dotenv()
telebot_token = os.getenv('TELEBOT_TOKEN')

bot = telebot.TeleBot(token=telebot_token,parse_mode=None)

#/start command handler
@bot.message_handler(commands=['start'])
def start_handler(message):
    """This function handles the /start command"""
    bot.reply_to(message,'Welcome to my bot')

# /help command handler
@bot.message_handler(commands=['help'])
def help_handler(message):
    """This function handles the /help command"""

    commands = """/start - Start the Bot.\n/ai - Ask the Bot a Question.\n/stream - Stream the Answer.\n/help - Get Help."""
    bot.reply_to(message, commands)

# /ai command handler
@bot.message_handler(commands=['ai']) 
def ai_handler(message): 
    """This function handles the /ai command"""

    if message.text == '/ai':
        bot.reply_to(message,'Please Use the format /ai question.')

    else:
        bot_message = bot.reply_to(message,'Please wait while I am processing your request')
        response = message_parser(message)

        bot.edit_message_text(response, chat_id=bot_message.chat.id,message_id=bot_message.message_id)

# /stream command handler
@bot.message_handler(commands=['stream'])
def stream_handler(message):
    """This function handles the /stream command"""
    prompt = message.text.replace('/test','')

    response_chunks = generate_response(prompt, stream=True)
    # send message to the user
    message = bot.reply_to(message, 'Please wait while I am processing your request')
    return message_streamer(message, response_chunks)


# test command handler
@bot.message_handler(commands=['test'])
def test_handler(message):
    """
    This function handles the /test command
    This is experimental feature.
    If is not working.
    Please use /ai command instead.
    """
    bot.reply_to(message,'This feature is not implemented yet, Only use n devlopment')
    raise NotImplementedError("This feature is not implemented yet, Only use in devlopment")

def message_streamer(original_message, stream_message):
    """This function tries to mimic stream like chatgt website"""
    msg = ''
    for chunk in stream_message:
        try:
            content = chunk['choices'][0]['delta']['content']
            msg += content
            if content in punctuation:
                bot.edit_message_text(msg, chat_id=original_message.chat.id, message_id=original_message.message_id)
        except KeyError:
            print("error")
    try:
        bot.edit_message_text(msg, chat_id=original_message.chat.id, message_id=original_message.message_id)
    except:
        time.sleep(0.5)

def message_parser(message):
    """This function parses the message and returns the response"""
    refine_message = f"{message.text.replace('/ai','')}" 
        
    if (refine_message.startswith('??') and 'program' in refine_message) or (refine_message.startswith('??') and 'code' in refine_message) :
        response = generate_response(refine_message)     
        return response

    if 'program' in refine_message or 'code' in refine_message:
        refine_message += 'give algorithm not code'
        response = generate_response(refine_message)
        return response

    response = generate_response(refine_message)
    return response