import os
import ctypes
import time

import pyautogui
import telebot
from telebot import types
import config
import keyboard


bot = telebot.TeleBot(config.TOKEN)
bot.send_message(config.CHAT_ID, "Bot online")


@bot.message_handler(commands=["start", "help"])
def start(message):
    rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = [["pause", "quiet", "loud", "<-", "->"]]

    if btns:  # Check that the list of btns is not empty
        rmk.row(*btns[0])
    bot.send_message(message.chat.id,
        """
        Hi, this is a universal remote controller to help you manage your computer from your phone
        
        pause - pauses the video
        quiet - makes the sound go quiet
        loud - makes the sound go louder
        <- - rewinds your video back 
        -> - rewinds your video forward
         
        write /start
        """,
        reply_markup=rmk
    )


command_actions = {
    "pause": lambda: keyboard.press('space'),
    "quiet": lambda: keyboard.press_and_release('volume down'),
    "loud": lambda: keyboard.press_and_release('volume up'),
    "<-": lambda: keyboard.press_and_release('left arrow'),
    "->": lambda: keyboard.press_and_release('right arrow')
}

@bot.message_handler(func=lambda m: m.text and m.text.lstrip('/').lower() in command_actions)
def handle_command(message):
    cmd = message.text.lstrip('/').lower()
    action = command_actions.get(cmd)
    if action:
        action()
    # Delete user message
    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception:
        bot.send_message(message.chat.id, "Something went wrong")

def sms_to_client(message):
    try:
        pyautogui.alert(message.text, "Message")
    except Exception:
        bot.send_message(message.chat.id, "Something went wrong")


# @bot.message_handler(commands=["input"])
# def send_message_with_answer(message):
# 	msg = bot.send_message(message.chat.id, "Enter the message:")
# 	bot.register_next_step_handler(msg)
#


# @bot.message_handler(commands=["wallpaper"])
# def wallpaper(message):
# 	msg = bot.send_message(message.chat.id, "Send a picture")
# 	bot.register_next_step_handler(msg, set_wallpaper)


# @bot.message_handler(content_types=["photo"])
# def set_wallpaper(message):
# 	file = message.photo[-1].file_id
# 	file = bot.get_file(file)

    # download_file = bot.download_file(file.file_path)
    # with open("image.jpg", "wb") as img:
    # 	img.write(download_file)
    #
    # path = os.path.abspath("image.jpg")
    # ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)
