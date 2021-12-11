import os

from telegram.ext import Updater, MessageHandler, Filters
from youtubeBot.utils import download_youtube_file


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
    """dictionary to save the songs and their names"""
    exist_video = {}

    def __init__(self, token):
        super().__init__(token)

    def message_handler(self, message):
        """check if the is song already been downloaded ,
        if not add the song and the song name to the dict"""

        if message in self.exist_video.keys():
            super().send_text(message + ' is already exist')
            super().send_video(self.exist_video[message])

        else:
            super().send_text(message + ' is downloading now, please wait  ')
            song = download_youtube_file(message, 1)
            self.exist_video[message] = song[0]
            super().send_video(song[0])


if __name__ == '__main__':
    YoutubeBot('')
