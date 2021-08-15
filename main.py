import RPi.GPIO as GPIO
import telebot
import key

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, GPIO.HIGH)
stat = False
bot = telebot.TeleBot(key.token)
@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "enable":
        print (message.from_user.id)
        print (c.stat)
        c.stat = True
        bot.send_message(message.from_user.id, "I'll turn it on now")
        GPIO.output(20, GPIO.LOW)
    elif message.text == "disable":
        c.stat = False

        bot.send_message(message.from_user.id, "turning it off")
        GPIO.output(20, GPIO.HIGH)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "disable/enable/status")
    elif message.text == "status":
        if c.stat == False:

            bot.send_message(message.from_user.id, "lights are OFF")
        else:
            print (c.stat)
            bot.send_message(message.from_user.id, "lights are ON")
    elif message.text == "admin":
        if message.from_user.id == 201265163:
            bot.send_message(message.from_user.id, "enter your password")
            if message.text == "admin":
                print('enter the command')
        else:
            bot.send_message(message.from_user.id, "you don't have access rights")
    else:
        bot.send_message(message.from_user.id, 'write /help.')
class stat:
    def __init__(self):
        self.stat = False
        print ("False")
    def en(self):
        self.stat = True
        prinf ("True")
    def dis(self):
        self.stat = False
        prinf ("False")
c = stat()
bot.polling(none_stop=True, interval=0)
