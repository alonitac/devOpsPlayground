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

    def __init__(self, token):
        self.ctr = 0
        self.videos = []
        super().__init__(token)

    def message_handler(self, message):
        if(self.ctr == 0):
             super().send_text('Downloading ' + message)
             self.videos = download_youtube_file(message, 2)
             super().send_text(self.videos)
             super().send_text('choose video index')
             self.ctr += 1

        else:
            if(int(message) < len(self.videos)):
                super().send_text('sending')
                super().send_video(self.videos[int(message)])
                self.ctr = 0
            else:
                super().send_text('pick another index')

if __name__ == '__main__':
    myBot = YoutubeBot()

