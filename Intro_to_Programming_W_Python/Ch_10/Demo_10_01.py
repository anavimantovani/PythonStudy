
FILE_NAME = 'MyFile.txt'

def main():
    #print('Hello world!')

    output_file = open(FILE_NAME, 'w')

    output_file.write('Hello world!\n')
    output_file.write('AAA\n')
    output_file.write('BBB\n')
    output_file.write('CCC\n')
    output_file.write('DDD\n')
    output_file.write('Goodbye.\n')


    output_file.close()



main()
