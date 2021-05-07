import telebot
bot = telebot.TeleBot("1802139186:AAG5dN1_lzT8hquhY3qu_sRSiE8kIE4MF4I")


def log(message):
    print("<!------!>")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name,
                                                              message.from_user.last_name,
                                                              str(message.from_user.id), message.text))





@bot.message_handler(commands = ["start"])

def cmd_start(message):
    bot.send_message(message.from_user.id, 'Привет')
    log(message)




bot.polling()
