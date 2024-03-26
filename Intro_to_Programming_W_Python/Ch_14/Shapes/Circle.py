
import math
from Shape import Shape

class Circle (Shape):

    def __init__(self):
        self.__radius = 0.0
        Shape.__init__(self)

    def set_radius(self, value):

        if value < 0:
            self.__radius = 0
        else:
            self.__radius = value

    def get_radius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def cirfumference(self):
        return math.pi * self.__radius * 2
