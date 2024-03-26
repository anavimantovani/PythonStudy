
SIZE = 5

def main():
    #numbers = [0, 0, 0, 0, 0]
    numbers = [0] * SIZE

    numbers[0] = 20
    numbers[1] = 30
    numbers[2] = 40
    numbers[3] = 50
    numbers[4] = 60

    numbers[2] = 400

    #print(numbers[0])
    #print(numbers[1])
    #print(numbers[2])
    #print(numbers[3])
    #print(numbers[4])

    for counter in range(0, SIZE):
        print(numbers[counter])



main()
