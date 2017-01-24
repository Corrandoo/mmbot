from threading import Thread
import config, telebot

bot = telebot.TeleBot(config.token)


def polling():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    thread1 = Thread(target=polling)
    thread1.start()