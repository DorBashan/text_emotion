from logic.srt_file_splitter import SrtFileSplitter
from logic.video_splitter import VideoSplitter

if __name__ == '__main__':
    srt_file_splitter = SrtFileSplitter()
    srt_parts = srt_file_splitter.split('logic/example_video.srt')

    s = VideoSplitter()
    s.split('logic/example_video.mp4', srt_parts)
