from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "Whats up",):
        return "Hello! How Are Ya?"

    if user_message in ("Who are You", "Who are You?"):
            return "I have Been Created By elias and Iam a Bot"

    if user_message in ("time," "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "it is not a chat room, iam a Youtube Downloader Paste ur LINK..."


