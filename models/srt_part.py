
class SrtPart:

    def __init__(self):
        self.index = -1
        self.start = -1
        self.end = -1
        self.text = ''

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def set_start(self, start):
        self.start = start

    def get_start(self):
        return self.start

    def set_end(self, end):
        self.end = end

    def get_end(self):
        return self.end

    def set_text(self, text):
        self.text = text

    def add_text(self, text):
        if text:
            self.set_text(self.get_text() + '\n' + text)
        else:
            self.set_text(text)

    def get_text(self):
        return self.text
