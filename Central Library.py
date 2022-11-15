class library:

    def __init__(self, listofbooks):
        self.book = listofbooks

    def available_books(self):
        print("Books available in Central Library are: ")
        for book in self.book:
            print(" * ",book)

    def borrow_book(self, bookName):
        if bookName in self.book:
            print(f'You have been issued {bookName} book.please keep it safe and return within 30 Days')
            self.book.remove(bookName)
            return True
        else:
            print(f'Sorry, this book is not aveilable either issued by someone, please wait until the book available')
            return False

    def return_book(self, bookName):
        self.book.append(bookName)
        print("Thanks, for returning/donating this book. Have a nice day ahead!!!")

class student:
    def requestbook(self):
        self.book=input("Enter the name of the book you want to borrow: ")
        return self.book
    def return_book(self):
        self.book=input("Enter the name of the book you want to return/donate: ")
        return self.book

if __name__=="__main__":
    Central_Library=library(["Python","Django","Java","Java Script","C","c++"])
    student=student()

    while(True):
        welcomemsg = '''\n*****Welcome to Central Library*****
        Please choose an option:
        1. list of all the books
        2. Borrow book
        3. Add/Return Book
        4. Exit the Library

        '''
        print(welcomemsg)
        a=int(input("Enter choice: "))
        if a == 1:
              Central_Library.available_books()
        elif a== 2:
            Central_Library.borrow_book(student.requestbook())
        elif a==3:
            Central_Library.return_book(student.return_book())
        elif a==4:
            exit()
        else:
            print("you entered a wrong value")
    
