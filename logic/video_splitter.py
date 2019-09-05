import os
import pathlib

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip, ffmpeg_extract_audio

from logic.srt_file_splitter import SrtFileSplitter


class VideoSplitter:

    def split(self, video_name, video_file_path, srt_parts):
        for part in srt_parts:
            start_seconds = self.convert_time_to_seconds(part.get_start())
            end_seconds = self.convert_time_to_seconds(part.get_end())
            dir_path = os.path.abspath(os.curdir)
            directory = "videos_data/%s/parts" % video_name
            full_directory = os.path.join(dir_path, directory)
            if not os.path.exists(full_directory):
                pathlib.Path(full_directory).mkdir(parents=True, exist_ok=True)
            ffmpeg_extract_subclip(video_file_path, start_seconds, end_seconds,
                                   targetname='%s/part_%s.mp4' % (full_directory,
                                                                  part.get_index()))
            full_directory_wav = os.path.join(dir_path, "videos_data/%s/parts_wav" % video_name)
            if not os.path.exists(full_directory_wav):
                pathlib.Path(full_directory_wav).mkdir(parents=True, exist_ok=True)

            try:
                ffmpeg_extract_audio('%s/part_%s.mp4' % (full_directory,
                                                         part.get_index()),
                                     output='%s/part_%s.wav' % (full_directory_wav, part.get_index()))
            except:
                pass

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
