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

    if message.text == "status":
        if stat:
            bot.send_message(message.from_user.id, "lights are OFF")
        else:
            bot.send_message(message.from_user.id, "lights are ON")
    elif message.text == "enable":
        stat = True
        bot.send_message(message.from_user.id, "I'll turn it on now")
        GPIO.output(20, GPIO.LOW)
    elif message.text == "disable":
        stat = False
        bot.send_message(message.from_user.id, "turning it off")
        GPIO.output(20, GPIO.HIGH)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "disable/enable/status")
    else:
        bot.send_message(message.from_user.id, 'write /help.')
bot.polling(none_stop=True, interval=0)
print (stat)