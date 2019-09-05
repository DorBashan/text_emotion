from models.srt_part import SrtPart


class ColoredSrtPart(SrtPart):
    def __init__(self):
        super(ColoredSrtPart, self).__init__()
        self.color_hexa = ''

    def __init__(self, srt_part: SrtPart, color_hexa):
        super(ColoredSrtPart, self).__init__()

        self.set_index(srt_part.get_index())
        self.set_text(srt_part.get_text())
        self.set_start(srt_part.get_start())
        self.set_end(srt_part.get_end())
        self.set_color(color_hexa)

    def set_color(self, color_hexa):
        self.color_hexa = color_hexa

    def get_color(self):
        return self.color_hexa

