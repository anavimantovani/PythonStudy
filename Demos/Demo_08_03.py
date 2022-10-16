

def main():
    scores = [60, 70, 90, 80, 100]

    #swap_elements_broken(scores[2], scores[3])
    swap_elements_correct(scores, 2, 3)

    for counter in range(0, len(scores)):
        print(counter, ':', scores[counter])


def swap_elements_correct(the_array, position1, position2):
    temp = the_array[position1]
    the_array[position1] = the_array[position2]
    the_array[position2] = temp


#def swap_elements_broken(value1, value2):
    #temp = value1
    #value1 = value2
    #value2 = temp


main()
