
#from Cat import Cat
#from Dog import Dog
#from Snake import Snake
from YorkshireTerrier import YorkshireTerrier

def main():

    a = YorkshireTerrier()
    a.set_name('Spike')

    print(a.get_name() + ' has ' + str(a.number_legs()) + ' legs, ', end='')

    if a.has_hair():
        print('has hair, ', end='')
    else:
        print('does not have hair, ', end='')

    print('and goes ' + a.sound() + '.')


main()
