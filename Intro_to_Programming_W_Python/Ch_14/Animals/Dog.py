
from Animal import Animal

class Dog (Animal):

    def __init__(self):

        Animal.__init__(self)

    def has_hair(self):
        return True

    def sound(self):
        return 'woof'
