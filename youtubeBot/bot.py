from telegram.ext import Updater, MessageHandler, Filters
from utils import download_youtube_file
from collections import defaultdict
import re
import os


class Bot:
    """
    purpose Cache2 to check if entered name again and reply to chad id the keyword hase entered its say its video exist
    """
    Cache2 = defaultdict()

    def __init__(self, token):
        updater = Updater(token, use_context=True)
        self.update = None
        self.context = None
        updater.dispatcher.add_handler(MessageHandler(Filters.text, self._callback))
        updater.start_polling()
        self.echo()
        print('Bot is running....')
        updater.idle()

    def echo(self):
        print("Welcome My Youtube Bot with Telegram Bot type Anything Name Audio And Will Be Send it")

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
        return self.update['message']

    def send_text(self, text):
        """Sends text to a chat"""
        self.update.message.reply_text(text)
        return self.update.message

    def send_message(self, message):
        self.context.bot.send_message(chat_id=self.update.message.chat_id, text=message)
        return self.update.message

    """
    method replay_message used for reply the text if the text entered again 
    """

    def replay_message(self, message):
        self.context.bot.send_message(chat_id=self.update.message.chat_id, text="The video is exist",
                                      reply_to_message_id=self.Cache2[message][2]['message_id'])

    def Delete_message(self, id):
        self.context.bot.deleteMessage(chat_id=self.update.message.chat_id, message_id=id)


class YoutubeBot(Bot):
    """
    Create defaultDict() because i want add Key without error and used for cache speed up my Program
    """
    Cache = defaultdict()
    """
    cwd is get the dir of default current projects
    """
    cwd = os.getcwd()
    """
    use methods ___init__ this help me to use Class youtube with class Bot and merg togther with token 
    """

    def __init__(self, token):
        Bot.__init__(self, token)

    """
    this message_handler methods used for ALG request the keyword in youtube and search to download and sent to telegram
    message and upload the audio/video in telegram 
    """

    """
    the purpose Cache used to key string and dir its help me to know where the file downloaded and check if
    this dir exist that file is values contains [1,name of file download]
    and check on way value 1 if exist and name file to exract the name     

    """

    def message_handler(self, message):

        if self.Cache.get(message + " " + self.cwd) is not None:
            if self.Cache[message + " " + self.cwd][1] == 1:
                Bot.replay_message(self, message)
        else:
            Bot.send_text(self, message)
            Bot.send_text(self, "please wait . ...")
            b = download_youtube_file(message)
            c = Bot.send_video(self, self.cwd + "/" + "".join(b))
            print(c)
            self.Cache[message + " " + self.cwd] = ["".join(b), 1]
            Bot.Cache2[message] = [1, "".join(b), c]


if __name__ == '__main__':
    # Bot('5059386927:AAFlC-c92t1DMjvcOzUCaYGNks337OcfMAE')
    b = YoutubeBot('5059386927:AAFlC-c92t1DMjvcOzUCaYGNks337OcfMAE')