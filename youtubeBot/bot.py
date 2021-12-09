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
    def message_handler(self, message):
        # start message in telegram with (vid 2:) to get one video
        if str(message).startswith("vid 1:"):
            youtube_search=message[6:]
            video_file = download_youtube_file(youtube_search)
            self.send_video(video_file[0])

        # start message in telegram with (vid 2:) to get two video's
        elif str(message).startswith("vid 2:"):
            youtube_search = message[6:]
            video_files = download_youtube_file(youtube_search, num_results=2)
            self.send_video(video_files[0])
            self.send_video(video_files[1])

        # start message in telegram with (vid 3:) to get three video's
        elif str(message).startswith("vid 3:"):
            youtube_search = message[6:]
            video_files = download_youtube_file(youtube_search, num_results=3)
            self.send_video(video_files[0])
            self.send_video(video_files[1])
            self.send_video(video_files[2])

        # doesnt start with a vid? then give me back the text as it is
        else:
            super().message_handler(message)


if __name__ == '__main__':
    my_token = open(".token").read()
    print(my_token)
    mybot = YoutubeBot(my_token)
