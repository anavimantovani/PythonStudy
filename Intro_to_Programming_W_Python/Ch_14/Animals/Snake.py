
from Animal import Animal

class Snake (Animal):

    def __init__(self):

        Animal.__init__(self)

    def number_legs(self):
        return 0

    def sound(self):
        return 'tsss'
