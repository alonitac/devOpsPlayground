
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
    requested_videos = {}
    def message_handler(self, message):
        "downloading the video"
        if  YoutubeBot.requested_videos.__contains__(message):
            print("downloading the requested video")
            _videos=download_youtube_file()
            YoutubeBot.requested_videos[message]=_videos
        else:
            print("the video is already downloaded, we will send the video in a seconds")
            _videos=YoutubeBot.requested_videos[message]
        self.send_video(_videos)

if __name__ == '__main__':
    YoutubeBot('')