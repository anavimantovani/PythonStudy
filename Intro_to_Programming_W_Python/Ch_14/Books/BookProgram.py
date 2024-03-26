
from Book import Book

def main():

    b1 = Book()

    book_input(b1)
    book_display(b1)


def book_input(bk):
    bk.title      = input('Enter title:          ')
    br.authors[0] = input('Enter author #1:      ')
    br.authors[1] = input('Enter author #2:      ')
    br.authors[2] = input('Enter author #3:      ')
    bk.isbn10     = input('Enter 10 digit ISBN:  ')
    bk.isbn13     = input('Enter 13 digit ISBN:  ')
    bk.msrp       = float(input('Enter MSRP:          '))


def book_display(bk):

    print()
    print()
    print('Title:            ', bk.title)
    print('Author #1:        ', bk.authors[0])
    print('Author #2:        ', bk.authors[1])
    print('Author #3:        ', bk.authors[2])
    print('ISBN 10:          ', bk.isbn10)
    print('ISBN 13:          ', bk.isbn13)
    print('MSRP:             ', bk.msrp)
    print()
    print()




main()
