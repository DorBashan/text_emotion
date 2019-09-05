import os

from logic.deep_effect import duplicate_wav, find_emotion
from logic.srt_file_splitter import SrtFileSplitter
from logic.subtitles_creator import SubtitlesCreator
from logic.subtitles_painter import SubtitlesPainter
from logic.video_splitter import VideoSplitter
from logic.youtube_utils.yt_utils import get_movie_and_sub_paths


def get_emotion(part):
    i = part.get_index()
    wav_file = os.path.join(dir_path, "videos_data/%s/parts_wav/part_%s.wav" % (video_name, i))
    if not os.path.exists(wav_file):
        return None
    # call function
    duplicate_wav(wav_file, wav_file)

    emotion = find_emotion(wav_file)
    return emotion


if __name__ == '__main__':
    srt_file_splitter = SrtFileSplitter()
    youtube_link = "https://www.youtube.com/watch?v=G7gklW3Xbn8"
    video_name = youtube_link.split('?v=')[1]
    movie_path, sub_path = get_movie_and_sub_paths(youtube_link)
    srt_parts = srt_file_splitter.split(sub_path)

    # split video to parts
    s = VideoSplitter()
    s.split(video_name, movie_path, srt_parts)

    parts_to_emotions = {}

    # take the parts and return srt_parts + emojis
    dir_path = os.path.abspath(os.curdir)
    for part in srt_parts:
        parts_to_emotions[part] = get_emotion(part)

    # use subtitles painter to get colors from emojits
    color_srt_parts = SubtitlesPainter.paint(parts_to_emotions)

    # use subtitles creator to create new srt file
    subtitle_input_path = os.path.join(dir_path, "videos_data/%s/full_sub/%s.srt" % (video_name, video_name))
    subtitle_output_path = os.path.join(dir_path, "videos_data/%s/full_video/%s.srt" % (video_name, video_name))
    SubtitlesCreator.create(subtitle_input_path, subtitle_output_path, color_srt_parts)
