
from Animal import Animal

class Cat (Animal):

    def __init__(self):

        Animal.__init__(self)

    def has_hair(self):
        return True

    def sound(self):
        return 'meow'
