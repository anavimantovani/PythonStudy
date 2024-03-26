
from Dog import Dog

class YorkshireTerrier (Dog):

    def __init__(self):

        Dog.__init__(self)

    def sound(self):
        return 'yip yap'


