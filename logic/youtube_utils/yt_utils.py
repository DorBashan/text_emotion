import os
import pathlib
from pytube import YouTube
import youtube_dl


def _download_caption(youtube_link):
    # download the package by:  pip install pytube

    source = YouTube(youtube_link)

    en_caption = source.captions.get_by_language_code('en')

    en_caption_convert_to_srt = (en_caption.generate_srt_captions()).encode('utf-8')

    # save the caption to a file named Output.txt
    directory = "videos_data/%s/full_sub" % source.video_id
    dir_path = os.path.abspath(os.curdir)

    full_path = os.path.join(dir_path, directory)
    if not os.path.exists(full_path):
        pathlib.Path(full_path).mkdir(parents=True, exist_ok=True)
    file_path = "%s/%s.srt" % (full_path, source.video_id)
    text_file = open(file_path, "wb")
    text_file.write(en_caption_convert_to_srt)
    text_file.close()
    return file_path


def _download_youtube_video(youtube_link):

    ydl_opts = {'outtmpl': 'videos_data/%(id)s/full_video/%(id)s.%(ext)s', 'format': 'mp4'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_link])
        return 'videos_data/%s/full_video/%s.mp4' % \
               (youtube_link.split('?v=')[1], youtube_link.split('?v=')[1])


def get_movie_and_sub_paths(youtube_link):
    return _download_youtube_video(youtube_link), _download_caption(youtube_link)
