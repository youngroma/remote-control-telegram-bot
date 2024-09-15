import os
import ctypes
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


@bot.message_handler(content_types=["text"])
def commands_handler(message):

	if message.text == "pause":
		presspause(message)
	elif message.text == "quiet":
		quieter(message)
	elif message.text == "loud":
		loud(message)
	elif message.text == "<-":
		back(message)
	elif message.text == "->":
		forward(message)


@bot.message_handler(commands=["PAUSE", "pause"])
def presspause(message):
	keyboard.press('space')

@bot.message_handler(commands=["quiet"])
def quieter(message):
	keyboard.press_and_release('volume down')
@bot.message_handler(commands=["loud"])
def loud(message):
	keyboard.press_and_release('volume up')

@bot.message_handler(commands=["<-"])
def back(message):
	keyboard.press_and_release('left arrow')

@bot.message_handler(commands=["->"])
def forward(message):   
	keyboard.press_and_release('right arrow')



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
