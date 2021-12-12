from telegram.ext import Updater, MessageHandler, Filters
from youtubeBot.utils import download_youtube_file


"""
Get the token to access the Api.
"""


def gettoken():
    try:
        token_text = open('TOKEN.txt', 'r')
        my_token = token_text.read().split('=')[1]

    except Exception as err:
        print(err)
    finally:
        # if token_text is defined - not null - has an instance assigned to it...
        if token_text:
            token_text.flush()
            token_text.close()
    return my_token


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

        self.context.bot.send_video(chat_id=self.update.message.chat_id, video=open(file_path, 'rb'),
                                    supports_streaming=True)

    def send_text(self, text):
        """Sends text to a chat"""
        self.update.message.reply_text(text)


class YoutubeBot(Bot):
    pass  # TODO your code here!

    # no need to define a constructor , default constructor will be generated .

    # static variable -- Dictionary hold previous videos as pairs {message: video path}.
    downloadedVideos = {}

    def message_handler(self, message):

        """Main messages handler"""
        # step 1 - download the requested video.

        if not YoutubeBot.downloadedVideos.__contains__(message):
            print("Downloading Video ...\n")
            video_name = download_youtube_file(message)[0]
            YoutubeBot.downloadedVideos[message] = video_name
        else:
            print('video will be sent directly no download needed..')
            video_name = YoutubeBot.downloadedVideos[message]

        # step 2 - replay back to the user .

        self.send_video(video_name)


if __name__ == '__main__':
    myBoot = YoutubeBot(gettoken())

