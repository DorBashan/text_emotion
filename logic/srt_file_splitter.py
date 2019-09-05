from typing import List

from models.srt_part import SrtPart


class SrtFileSplitter:

    def split(self, srt_file_name) -> List[SrtPart]:
        f = open(srt_file_name, "r")
        line_reader = f.readlines()
        parts = []

        index = 1
        srt_part = SrtPart()
        for line in line_reader:
            if line == '\n':
                continue
            if index % 3 == 1:
                srt_part.set_index(int(line))
            if index % 3 == 2:
                divided_times = line.split('-->')
                start_str = divided_times[0]
                end_str = divided_times[1]
                srt_part.set_start(start_str.split(',')[0].strip())
                srt_part.set_end(end_str.split(',')[0].strip())
            if index % 3 == 0:
                srt_part.set_text(line)
                parts.append(srt_part)
                srt_part = SrtPart()

            index = index + 1
        return parts


if __name__ == '__main__':
    spliter = SrtFileSplitter()
    spliter.split('resources/example_video.srt')

