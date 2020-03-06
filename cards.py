
class Card:
    def __init__(self, color, mark, image_path):
        self.color = color
        self.mark = mark
        self.image_path = image_path

    def __str__(self):
        return self.color + self.mark

    def get_color(self):
        return self.color

    def get_mark(self):
        return self.mark

    def get_image_path(self):
        return self.image_path

    def display(self, x, y, win):
        pass
