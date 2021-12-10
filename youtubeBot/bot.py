from telegram.ext import Updater, MessageHandler, Filters
from youtubeBot.utils import download_youtube_file
from youtube_dl import YoutubeDL
import os

class Bot:
    def __init__(self, token):
        updater = Updater(token, use_context=True)
        self.update = None
        self.context = None
        updater.dispatcher.add_handler(MessageHandler(Filters.text, self._callback))
        updater.start_polling()
        print('Bot is running....')
        updater.idle()


    def _callback(self, update, context):
        """Internal method to handle received messages"""
        self.update = update
        self.context = context
        self.message_handler(update.message.text)

    def message_handler(self, message):
        """Main messages handler"""
        self.send_text(message)

    def send_video(self, file_path):
        """Sends video to a chat"""
        self.context.bot.send_video(chat_id=self.update.message.chat_id, video=open(file_path, 'rb'), supports_streaming=True)

    def send_text(self, text):
        """Sends text to a chat"""
        self.update.message.reply_text(text)


class YoutubeBot(Bot):
    def __init__(self, token, library):
        self.library = library
        updater = Updater(token, use_context=True)
        self.update = None
        self.context = None
        updater.dispatcher.add_handler(MessageHandler(Filters.text, self._callback))
        updater.start_polling()
        print('Bot is running....')
        updater.idle()

    def list_files(self):
        """
        List book id's
        :return:
        """
        files = os.listdir(self.library)
        return files

    def message_handler(self, message):
        """Main messages handler"""
        is_exist = False
        for file in self.list_files():
             if file.__contains__(message):
                 self.send_text('you already downloaded this file')
                 is_exist = True
                 break
        if is_exist == False:
            downloaded_videos = download_youtube_file(message)
            for file in self.list_files():
                if file.__contains__(message):
                    self.send_video(file)
                    break




if __name__ == '__main__':
    token = open('.token').read()


