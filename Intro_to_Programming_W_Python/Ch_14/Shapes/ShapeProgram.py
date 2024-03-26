
#from Rectangle import Rectangle
#from Square import Square
from Circle import Circle

def main():
    shape1 = Circle()

    shape1.pos_x = 120
    shape1.pos_y = 240
    shape1.color = 'Red'
    shape1.set_radius(5)
    #shape1.set_length(5)
    #shape1.set_width(10)

    print()
    print('Position:      ' + str(shape1.pos_x) + ', ' + str(shape1.pos_y))
    print('Color:         ' + shape1.color)
    #print('Length:        ' + str(shape1.get_length()))
    #print('Width:         ' + str(shape1.get_width()))
    print('Radius:        ' + str(shape1.get_radius()))
    print('Area:          ' + str(shape1.area()))
    print('Circumference: ' + str(shape1.cirfumference()))


main()
