from typing import List

from models.colored_srt_part import ColoredSrtPart
from shutil import copyfile

from models.srt_part import SrtPart


class SubtitlesCreator:

    @staticmethod
    def create(input_file_path, output_file_path, parts: List[ColoredSrtPart]):

        f = open(input_file_path, "r")
        line_reader = list(f.readlines())
        f.close()

        item = {}
        lst = []
        index = 1

        for line in line_reader:
            if line == '\n':
                index = 1
                lst.append(item)
                item = {}
                continue
            if index == 1:
                item['index'] = int(line)
            if index == 2:
                item['time'] = line
            if index > 2:
                if 'text' not in item:
                    item['text'] = []
                item['text'].append(line.replace('\n',''))
            index = index + 1

        f = open(output_file_path, "w")

        for item in lst:
            i = item['index']
            curr_part = [x for x in parts if x.get_index() == i]
            if curr_part:
                current_color = curr_part[0].get_color()
            else:
                current_color = '#000000'
            color_line = '<font color="{}">'.format(current_color)
            close_color_line = '</font>'
            f.write(str(i) + '\n')
            f.write(item['time'].replace('\n', '') + '\n')
            f.write(color_line.replace('\n', '') + "\n")
            f.write('\n'.join(item['text']))
            f.write(close_color_line.replace('\n', '') + "\n")
            f.write('\n')

        f.close()

        # copyfile(input_file_path, output_file_path)
        #
        # f = open(input_file_path, "r")
        # contents = f.readlines()
        # f.close()
        #
        # f = open(input_file_path, "r")
        # line_reader = f.readlines()
        #
        # globals_index_to_colors = []
        # globals_index_to_close_font_symbol = []
        #
        # current_index = 1
        # current_color = ''
        # global_index = 0
        # for line in line_reader:
        #     if current_index == 1:
        #         parts = [x for x in parts if x.get_index() == int(line)]
        #         if parts:
        #             current_color = parts[0].get_color()
        #         else:
        #             current_color = '#000000'
        #     if current_index == 2:
        #         globals_index_to_colors.append(tuple((global_index + 1, current_color)))
        #     if line == '\n':
        #         globals_index_to_close_font_symbol.append(global_index + 1)
        #         current_index = 1
        #         global_index = global_index + 1
        #         continue
        #
        #     current_index = current_index + 1
        #     global_index = global_index + 1
        #
        # globals_index_to_close_font_symbol.append(global_index + 1)
        #
        # f.close()
        #
        # for index, color in globals_index_to_colors:
        #     contents.insert(index, '<font color="{}">'.format(color))
        #
        # for index in globals_index_to_close_font_symbol:
        #     contents.insert(index, '</font>')
        #
        # f = open(output_file_path, "w")
        # contents = "".join(contents)
        # f.write(contents)
        # f.close()


if __name__ == '__main__':
    part = SrtPart()
    part.set_index(1)
    l = [ColoredSrtPart(part, '#ff0000')]
    SubtitlesCreator.create('pulp_test.srt', 'output.srt', l)
