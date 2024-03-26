
from Shape import Shape

class Rectangle (Shape):

    def __init__(self):
        self.__length = 0.0
        self.__width = 0.0
        Shape.__init__(self)


    def set_length(self, value):
        self.__length = value

    def set_width(self, value):
        self.__width = value

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def area(self):
        return self.__length * self.__width

    def cirfumference(self):
        return 2 * (self.__length + self.__width)
