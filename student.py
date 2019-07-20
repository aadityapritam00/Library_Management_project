import time
class Student:
    def __init__(self):
        self.name=input("Enter Student Name\t\t\t\t:")
        self.enroll=input("Enter your Enrollment No\t\t:")
        self.sem=int(input("Enter your semester(in integer only)\t:"))
        self.branch=input("Enter your branch\t\t\t:")
        self.issued_book=[]
        
        
    def view_profile_student(self):
        print("\n-------------------------------------DASHBOARD----------------------------------------")
        time.sleep(3)
        print(f"\n\tName:  {self.name}\t\t\tEnrollment No:  {self.enroll}\n\tSemester:  {self.sem}\t\t\tBranch:  {self.branch}\n\tBook Issued:  {self.issued_book}")
        print("____________________________________________x___________________________________________")             
   

   