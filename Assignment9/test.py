import telebot
import random
import gtts
from telebot import types


bot = telebot.TeleBot("6538407565:AAFlb2ale8ahbORtudLLNvtvwkoI_VYhZ-k",parse_mode=None)

keyboard = types.ReplyKeyboardMarkup(row_width=3)
itembtn1 = types.KeyboardButton('back')
itembtn2 = types.KeyboardButton('/fal')
itembtn3 = types.KeyboardButton('help')
itembtn4 = types.KeyboardButton('voice')
itembtn5 = types.KeyboardButton('')
itembtn6 = types.KeyboardButton('')
keyboard.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy! how are u doing today?")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "What can I do for you?")

@bot.message_handler(commands=['fal'])
def send_fal(message):
    fal_list=["your going to a trip", "your gonna get laid", "your gonna get fucked"]
    selected_fal=random.choice(fal_list)
    bot.send_message(message.chat.id, selected_fal)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    #bot.reply_to(message,"This is a simple message.")
    if message.text == "salam":
        bot.send_message(message.chat.id, "AleykSalam!")
    elif message.text == "khubi?":
        bot.send_message(message.chat.id, "Na faghat to khubi!")
    elif message.text == "dooset daram":
        bot.send_message(message.chat.id, "mnm hamintor")
    elif message.text == "axe ghadi bede":
        photo = open("khoshgele.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "I can`t understand you.", reply_markup=keyboard)



bot.infinity_polling()


