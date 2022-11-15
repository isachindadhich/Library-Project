# Library-Project
My first project using Python. In this we can borrow a book from library and also we can submit(donate)..
class library:
  def __init__(self,listofbooks):
    self.book=listofbooks
  def available_books(self):
    print("Books available in Central Library are: ")
    for book in self.books:
      print(" * ",book)
  def borrow_book(self,bookName):
    if bookName in self.book:
      print(f'You issued {bookName} book. Please keep it safe')
      self.book.remove(bookName)
      return True
    else:
      print("Sorry this book is not available either issued by someone")
      return False
  def return_book(self,bookName):
    self.book.append(bookName)
    print("Thankyou for returning/donating this book. Have a nice day!!!.")
class student:
  def request_book(self):
    self.book=input("Enter the name of the book you want to borrow: ")
    return self.book
  def return_book(self):
    self.book=input("Enter the name of the book you want to return/donate: ")
    return self.book
if __name__=="__main__":
  Central_Libray=library(["Python","Django","java","C","C++","Java script"])
  student=student()
  while True:
  welcomemsg='''\n***Welcome to Central Library***
  Please choose an option:
  1. List of available books
  2. Borrow book
  3. Return/Donate book
  4. Exit the Library
  
  '''
  print(welcomemsg)
  a=int(input("Enter Your choice")
  if a ==1:
    Central_Library.available_book()
  elif a == 2:
    Central_Libraru.borrow_book(student.request_book())
  elif a == 3:
    Central_Library.return_book(student.return_book())
  elif a == 4:
    exit()
  else:
    print("You entered a wrong value")
    
    
    
    
    
    
    
