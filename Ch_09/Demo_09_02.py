

def main():
    example_array = [0.0] * 10

    example_array[0] = 20
    example_array[1] = 10

    temp = example_array[1]
    example_array[1] = example_array[0]
    example_array[0] = temp

    print('example_array[0] =', example_array[0])
    print('example_array[1] =', example_array[1])


main()
