from youtube_dl import YoutubeDL


def download_youtube_file(video_name, num_results=1):
    """
    This function downloads the first num_results search results from Youtube
    :param video_name: string of the video name
    :param num_results: integer representing how many videos to download
    :return: list of paths to your downloaded video files
    """

    with YoutubeDL({'format': 'bestaudio', 'noplaylist': 'True'}) as ydl:
        videos = ydl.extract_info(f"ytsearch{num_results}:{video_name}", download=True)['entries']

    return [ydl.prepare_filename(video) for video in videos]


# you can run the following line just for testing:

# downloaded_videos = download_youtube_file('gerara here man shit', num_results=2)
