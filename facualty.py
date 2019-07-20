import time
class Facualty:
    def __init__(self):
        self.fname=input("Enter Your Name \t\t:")
        self.fid=input("Enter your  Id   \t\t:")
        self.issued_book_facualty=[]
        
    def req_book(self):
        book_name=input("Enter the book name to put request")
        
        
    def view_profile_facualty(self):
        print("\n--------------------------------FACUALTY DASHBOARD----------------------------------------")
        time.sleep(3)
        print(f"\n\tName: {self.name}\tFacualty Id: {self.fid}\tBook Issued: {self.issued_book_facualty}")
        print("____________________________________________x___________________________________________")             
