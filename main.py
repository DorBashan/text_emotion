from logic.srt_file_splitter import SrtFileSplitter
from logic.video_splitter import VideoSplitter
from logic.youtube_utils.yt_utils import get_movie_and_sub_paths

if __name__ == '__main__':
    srt_file_splitter = SrtFileSplitter()
    youtube_link = "https://www.youtube.com/watch?v=x2WK_eWihdU"
    video_name = youtube_link.split('?v=')[1]
    movie_path, sub_path = get_movie_and_sub_paths(youtube_link)
    srt_parts = srt_file_splitter.split(sub_path)

    s = VideoSplitter()
    s.split(video_name, movie_path, srt_parts)
