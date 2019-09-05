from typing import List

from models.colored_srt_part import ColoredSrtPart
from shutil import copyfile

from models.srt_part import SrtPart


class SubtitlesCreator:

    @staticmethod
    def create(input_file_path, output_file_path, parts: List[ColoredSrtPart]):

        copyfile(input_file_path, output_file_path)

        f = open(input_file_path, "r")
        contents = f.readlines()
        f.close()

        f = open(input_file_path, "r")
        line_reader = f.readlines()

        globals_index_to_colors = []
        globals_index_to_close_font_symbol = []

        current_index = 1
        current_color = ''
        global_index = 0
        for line in line_reader:
            if current_index == 1:
                part = [x for x in parts if x.get_index() == int(line)][0]
                current_color = part.get_color()
            if current_index == 2:
                globals_index_to_colors.append(tuple((global_index + 1, current_color)))
            if line == '\n':
                globals_index_to_close_font_symbol.append(global_index + 1)
                current_index = 1
                global_index = global_index + 1
                continue

            current_index = current_index + 1
            global_index = global_index + 1

        globals_index_to_close_font_symbol.append(global_index + 1)

        f.close()

        for index, color in globals_index_to_colors:
            contents.insert(index, '<font color="{}">'.format(color))

        for index in globals_index_to_close_font_symbol:
            contents.insert(index, '</font>')

        f = open(output_file_path, "w")
        contents = "".join(contents)
        f.write(contents)
        f.close()


if __name__ == '__main__':
    part = SrtPart()
    part.set_index(1)
    l = [ColoredSrtPart(part, '#ff0000')]
    SubtitlesCreator.create('pulp_test.srt', 'output.srt', l)

