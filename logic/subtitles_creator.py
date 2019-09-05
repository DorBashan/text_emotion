from typing import List

from models.colored_srt_part import ColoredSrtPart
from shutil import copyfile


class SubtitlesCreator:

    def create(self, input_file_path, output_file_path, parts: List[ColoredSrtPart]):

        copyfile(input_file_path, output_file_path)

        f = open(output_file_path, "a+")

        for part in parts:
            f.write('test')
