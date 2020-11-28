from threading import *

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


class Listener:
    def __init__(self, telegram_handle):
        self.user_id = telegram_handle
        self.updater = Updater("TOKEN GOES HERE", use_context=True)
        self.polling = Thread(target = self.updater.start_polling)
        self.new_message = False
        self.new_update_obj = {}


    def start_listening(self):
        def start(update: Update, context: CallbackContext):
            update.message.reply_text('Hope you make it back alive :=(')

        def handler(update: Update, context: CallbackContext):
            if update.message.from_user.username == self.user_id:
                self.new_message = True
                self.new_update_obj = update

        dispatcher = self.updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handler))
        self.polling.start()


    def get_new_update(self):
        update = {}
        if self.new_message:
            self.new_message = False
            update = self.new_update_obj
            self.new_update_obj = {}
        return update


    def stop_polling(self):
        self.updater.stop()


def main():
    listener = Listener("FatSushi21")


if __name__ == '__main__':
    main()
