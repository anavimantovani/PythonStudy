

class Animal:

    def __init__(self):
        self.__name = 'Unknown'

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def has_hair(self):
        return False

    def number_legs(self):
        return 4

    def sound(self):
        return 'a noise of some sort'
