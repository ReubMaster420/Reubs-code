import os


class book():
    def __init__(self, Title, Author, isbn, Fiction, LastRead):
        self.__Title = Title
        self.__Author = Author
        self.__isbn = isbn
        self.__Fiction = Fiction
        self.__LastRead = LastRead
    def show(self):
        print("Title:" ,self.__Title)
        print("Author:" ,self.__Author)
        print("ISBN:" ,self.__isbn)
        print("Fiction:" ,self.__Fiction)
        print("Last Read:" ,self.__LastRead)
    def showisbn(self):
        return self.__isbn

def hash(isbn):
    address = (isbn%2000 + 1)
    return address

def findbook():
    while True: 
        isbn1 = input("Input a 13 digit ISBN:")
        if len(isbn1) == 13:
            break
        else:
            print("Please put a 13 digit code.")
    books = []
    try:
        with open("/Users/reubenlarsen/Reubs-code/Exam Practice/MyBooks.txt","r") as whole_file:
            for line in whole_file:
                parts = line.split(",")
                books.append(book(*parts))
    except OSError:
            print("Sorry, could not find the file. Make sure it is in the correct directory. The current directory is",os.getcwd())
    for i in range(len(books)):
        if isbn1 in books[i].showisbn():
           books[i].show()


findbook()