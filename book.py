import time
class Book:
    def __init__(self):
        self.bname=input("Book Name\t:")
        self.isbn=input("ISBN No   \t:")
        self.no_copies=int(input("No of Books:"))
        
    def view_all_book(self):
        print("------------------------------📚 Book Records 📖---------------------------------")
        print("Loading.....................")
        time.sleep(3)
        print(f"Book Name: {self.bname}\nISBN No:{self.isbn}\nNo of Books{self.no_copies}")
        print("______________________________________***____________________________________________")
        