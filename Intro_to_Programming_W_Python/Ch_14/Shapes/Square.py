
from Rectangle import Rectangle

class Square (Rectangle):

    def __init__(self):
        Rectangle.__init__(self)

    def set_length(self, value):
        Rectangle.set_length(self, value)
        Rectangle.set_width(self, value)

    def set_width(self, value):
        Rectangle.set_length(self, value)
        Rectangle.set_width(self, value)


