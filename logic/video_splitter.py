from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

from logic.srt_file_splitter import SrtFileSplitter


class VideoSplitter:

    def split(self, video_file_path, srt_parts):
        for part in srt_parts:
            start_seconds = self.convert_time_to_seconds(part.get_start())
            end_seconds = self.convert_time_to_seconds(part.get_end())

            ffmpeg_extract_subclip(video_file_path, start_seconds, end_seconds,
                                   targetname='logic/parts/part_{}.mp4'.format(part.get_index()))

    @staticmethod
    def convert_time_to_seconds(time_str):
        splitted_time = time_str.split(":")
        seconds = int(splitted_time[2])
        minutes_to_seconds = int(splitted_time[1]) * 60
        hours_to_seconds = int(splitted_time[0]) * 60 * 60

        return seconds + minutes_to_seconds + hours_to_seconds

if __name__ == '__main__':
    srt_file_spliter = SrtFileSplitter()
    srt_parts = srt_file_spliter.split('example_video.srt')

    s = VideoSplitter()
    s.split('example_video.mp4', srt_parts)
