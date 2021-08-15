import RPi.GPIO as GPIO
import telebot
import key

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)

bot = telebot.TeleBot(key.token)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "status":
        if GPIO.output(17) == GPIO.HIGH:
            bot.send_message(message.from_user.id, "lights are ON")
        else:
            bot.send_message(message.from_user.id, "lights are OFF")
    elif message.text == "enable":
        bot.send_message(message.from_user.id, "I'll turn it on now")
        GPIO.output(17, GPIO.HIGH)
    elif message.text == "disable":
        bot.send_message(message.from_user.id, "turning it off")
        GPIO.output(17, GPIO.LOW)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Hi")
    else:
        bot.send_message(message.from_user.id, 'write /help.')
bot.polling(none_stop=True, interval=0)


if __name__=='__main__':
    while True:
        print("key.light")
        get_text_messages()

