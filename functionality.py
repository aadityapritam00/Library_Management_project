from book import *
from student import *
import facualty as fac
import pickle
import time
import os,sys
import os

# #############################################  Book  #################################################################

def request_book():
        flag=0
        flag1=0
        lb=[]
        ls=[]
        utype=input(" press: 'S' IF You Are Student\t\tF: IF You Are Facualty\t\t'E' for Exit\n")
        if utype=='S':
            bn=input("enter book name or ISBN No to put the Request: ")
            with open("book.pkl",'rb') as f:
                while(True):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if bn==i.bname or bn==i.isbn:
                                if i.no_copies==1:
                                    flag=1
                                else:
                                    flag1=1
                            lb.append(i)
                    except EOFError:
                        break
            if(flag==1 or flag1==1):
                for i in lb:
                    if(bn==i.bname or bn==i.isbn):
                        if flag==1:
                            lb.remove(i)
                        else:
                            i.no_copies-=1
                        break

                with open("book.pkl",'wb') as f:
                    pass
                with open("book.pkl",'ab') as f:
                    pickle.dump(lb,f)
                sn=input("Enter your Name or Enrollment No:")
                with open("student_record.pkl",'rb') as fs:
                    ss=pickle.load(fs)
                    for i in ss:
                        if i.name==sn or i.enroll==sn:
                            i.issued_book.append(bn)
                            with open("student_record.pkl",'wb') as fs:
                                pickle.dump(ss,fs)
                                print("Requested Successfully !")
                                break
            else:
                print("No such Books found")
                                   
        elif utype=='F':
            bn=input("enter book name or ISBN No to put the Request: ")
            with open("book.pkl",'rb') as f:
                while(True):
                    try:
                        obj=pickle.load(f)
                        for i in obj:
                            if bn==i.bname or bn==i.isbn:
                                if i.no_copies==1:
                                    flag=1
                                else:
                                    flag1=1
                            lb.append(i)
                    except EOFError:
                        break
            if(flag==1 or flag1==1):
                for i in lb:
                    if(bn==i.bname or bn==i.isbn):
                        if flag==1:
                            lb.remove(i)
                        else:
                            i.no_copies-=1
                        break

                with open("book.pkl",'wb') as f:
                    pass
                with open("book.pkl",'ab') as f:
                    pickle.dump(lb,f)
                sn=input("Enter Facualty Name or Id :")
                with open("facualty_record.pkl",'rb') as fs:
                    ss=pickle.load(fs)
                    for i in ss:
                        if i.fname==sn or i.fid==sn:
                            i.issued_book_facualty.append(bn)
                            with open("facualty_record.pkl",'wb') as fs:
                                pickle.dump(ss,fs)
                                print("Requested Successfully !")
                                break
        elif utype=='E':
            sys.exit()
        else:
            print("wrong key entered ❌")

def search_book():
        print("1>Enter Book Name or ISBN No to search: ")
        with open("book.pkl",'rb') as f:
            sb=input("Enter the Book Name or ISBN No to search")
            while(True):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.bname==sb or i.isbn==sb:
                            print("Book found")
                            print("Name\t\tISBN No\t\tAvailable copies")
                            print(i.bname,"\t\t",i.isbn,"\t\t",i.no_copies)
                            print("Select the key:\t1>Request Book\t2>Back\t3>Exit")
                            inp4=int(input())
                            if inp4==1:
                                request_book()
                            elif inp4==2:
                                break
                            elif inp4==3:
                                sys.exit()
                            else:
                                print("wrong key entered,try again")
                                return

                except EOFError:
                    print("record search completed")
                    break


def show_all_book():
    print("****************************Book Records***************************")
    with open ("book.pkl",'rb') as f:
        if os.path.isfile("book.pkl")==True:
            print("Book Name\t\tISBN No\t\t\tNo of Books")
            while(True):
                try:
                    objs=pickle.load(f)
                    for i in objs:
                        print(i.bname,"\t\t\t",i.isbn,"\t\t\t",i.no_copies)
                except EOFError:
                    print("\nAll Book Displayed\n")
                    break
            else:
                print("No file found")
                return



def remove_book():
        obj=None
        k=input("Enter Book ISBN or Book Name to Remove")
        l=[]
        f=0
        g=0
        with open("book.pkl",'rb') as f:
            while(True):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if k==i.bname or k==i.isbn:
                            if i.no_copies==1:
                                f=1
                            else:
                                g=1
                        l.append(i)
                except EOFError:
                    break
        if(f==1 or g==1):
            for i in l:
                if(k==i.bname or k==i.isbn):
                    if f==1:
                        l.remove(i)
                    else:
                        i.no_copies-=1
                    break

            with open("book.pkl",'wb') as f:
                pass
            with open("book.pkl",'ab') as f:
                pickle.dump(l,f)
                print("removed successfully")

        else:
            print("No such Books found")



def add_book():
        print("Please, Specify the Book detail to add")
        lst=[]
        obj2=Book()
        lst.append(obj2)
        with open("book.pkl",'ab') as f:
            pickle.dump(lst,f)
            print("Book Added🙍‍♂️\n")

def modify_book():
        obj=None
        while(True):
            print("1>Modify Book Name\n2>Modify Isbn no:\n3>Back\n4>Exit")
            inp=int(input())
            if inp==1:
                with open("book.pkl",'rb') as f:
                    flag=0
                    l=[]
                    bn=input("Enter book Name:")
                    while(True):
                        try:
                            obj=pickle.load(f)

                            for i in obj:
                                if bn==i.bname:
                                    flag=1
#                                     i.bname=input("ENTERN NEW NAME")
#                                     l.append(i)
#                                 else:
                                l.append(i)


#                                     i.bname=input("Enter the new name you want to modify")
#                                     print("Name modified successfully")
#                                 else:
#                                     print("No such book found")
#                                     break
                        except EOFError:
#                             print("Updated ucessfully")
                            break
                if(flag==1):
                    for i in l:
                        if bn==i.bname:
                            i.bname=input("enter new name")
                            break

                    with open("book.pkl",'wb') as f:
                        pass
                    with open("book.pkl",'ab') as f:
                        pickle.dump(l,f)
                        print("Updated ucessfully")
            elif inp==2:
                print("🚫Access denied,you can't change ISBN No of a book")
            elif inp==3:
                break
            elif inp==4:
                sys.exit()
            else:
                print("Wrong key entered, enter again")
                break
# ############################################# Student  ####################################################

def add_student():
        lst1=[]
        obj1=Student()
        lst1.append(obj1)
        with open("student_record.pkl",'ab') as f:
            pickle.dump(lst1,f)
            print("Student Added🙍‍♂️\n")


def eliminate_student():
        flag=0
        lst=[]
        while(True):
            print("1>Eliminate by Student Name\n2>Eliminate By Enrollment No:\n3>Exit")
            inp=int(input())
            if inp==1:
                sm=input("Enter the name of student to eliminate: ")
                with open("student_record.pkl",'rb') as f:
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                if i.name==sm:
                                    flag=1

                                lst.append(i)

                        except EOFError:
                            print("File end")
                            break
                if flag==1:
                    for i in lst:
                        if i.name==sm:
                            lst.remove(i)

                    with open("student_record.pkl",'wb') as f:
                        pass
                    with open("student_record.pkl",'ab') as f:
                        pickle.dump(lst,f)
                        print("student is eliminated from record")
                        break


            if inp==2:
                en=input("Enter the enrollment No to eliminate student:")
                with open("student_record.pkl",'rb') as f:
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                if i.enroll==en:
                                    flag=1
                                else:
                                    print("student of this enrollmebt no not found")
                                    break
                            lst.append(i)

                        except EOFError:
                            print("File end")
                            break
                if flag==1:
                    for i in lst:
                        if i.enroll==en:
                            lst.remove(i)

                    with open("student_record.pkl",'wb') as f:
                        pass
                    with open("student_record.pkl",'ab') as f:
                        pickle.dump(lst,f)
                        break
            if inp==3:
                break



def update_student():
            lss=[]
            fg=0
            fg1=0
            print("1>Update Student Name\n2>Update Semester\n3>Update Branch\n4>Issue Book\n5>Exit")
            inp=int(input())
            if inp==1:
                bn=input("Enter the student name to update")
                with open("student_record.pkl",'rb') as f:
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                if i.name==bn:
                                    fg=1
#                                     i.name=input("Enter Student's New Name:")
                                lss.append(i)
                        except EOFError:
                            print("End")
                            break
                if fg==1:
                    for i in lss:
                        if i.name==bn:
                            i.name=input("Enter New Name of Student: ")
                            break

                        with open("student_record.pkl",'wb') as f:
                            pass
                        with open("student_record.pkl",'ab') as f:
                            pickle.dump(lss,f)

            elif inp==2:
                bn=input("Enter the student's semester to update")
                with open("student_record.pkl",'rb') as f:
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                if i.sem==bn:
                                    fg=1
#                                     i.name=input("Enter Student's New Name:")
                                lss.append(i)
                        except EOFError:
                            print("End")
                            break
                if fg==1:
                    for i in lss:
                        if i.sem==bn:
                            i.sem=int(input("Enter New Name of Student(in integer only): "))

                        with open("student_record.pkl",'wb') as f:
                            pass
                        with open("student_record.pkl",'ab') as f:
                            pickle.dump(lss,f)
#                 bn=input("Enter the Name of student whose Enrollment No is update:")
#                 with open("student_record.pkl",'rb') as f:
#                     while(True):
#                         try:
#                             obj=pickle.load(f)
#                             for i in obj:
#                                 if i.name==bn:
#                                     i.enroll=input("New Enroll No:")
#                                 else:
#                                     print("student not  exist,plz try again")
#                                     break
#                         except EOFError:
#                             print("student record End")
#                             break
#                     with open("student_record.pkl",'ab') as f:
#                         pickle.dump(obj,f)

            elif inp==3:
                bn=input("Enter the student Branch to change: ")
                with open("student_record.pkl",'rb') as f:
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                if i.branch==bn:
                                    fg=1
#                                     i.name=input("Enter Student's New Name:")
                                lss.append(i)
                        except EOFError:
                            print("End")
                            break
                if fg==1:
                    for i in lss:
                        if i.branch==bn:
                            i.branch=input("Enter New Name of Student: ")

                        with open("student_record.pkl",'wb') as f:
                            pass
                        with open("student_record.pkl",'ab') as f:
                            pickle.dump(lss,f)
            elif inp==4:
                bn=input("Enter Student name to issue book:")
                with open("student_record.pkl",'rb') as f:
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                if i.name==bn:
                                    fg=1
                                else:
                                    print("Student not found ,plz try again")
                                    break
                        except EOFError:
                            print("students records End")
                            break
                if fg==1:
                    for i in lss:
                        if i.name==bn:
                            ib=input("Enter the book name to issue")
                            with open("book.pkl",'rb') as fb:
                                b=pickle.load(fb)
                                for j in b:
                                    if j.bname==ib:
                                        i.issued_book=ib
                    with open("student_record.pkl",'wb') as f:
                        pass
                    with open("student_record.pkl",'ab') as f:
                        pickle.dump(lss,f)

            elif inp==5:
                sys.exit()

            else:
                print("Wrong key entered, please try correct key")
                return

def view_all_student():
    print("\n****************************Students Records***************************")
    with open ("student_record.pkl",'rb') as f:
        if os.path.isfile("student_record.pkl")==True:
            print("\nStudent Name\t\tEnrollment No\t\tSemester\t\tBranch\t\t\tIssued Books")
            while(True):
                try:
                    objk=pickle.load(f)
                    for i in objk:
                        print(i.name,"\t",i.enroll,"\t",i.sem,"\t\t\t",i.branch,"\t\t\t\t\t",i.issued_book)
                except EOFError:
                    print("\nAll Students  Displayed\n")
                    return
        else:
            print("No file found")


def view_search_student():
    f1=0
    with open("student_record.pkl",'rb') as f:
        if os.path.isfile("student_record.pkl")==True:
            sname=input("Enter Name or Enrollment No to view profile:")
            while(True):
                try:
                    objk=pickle.load(f)
#                     sname=input("Enter Name or Enrollment No to view profile:")
                    for i in objk:
                        if i.name==sname or i.enroll==sname:
                            print("\nName\tEnrollment No\tSemester\tBranch\t\tIssued Books")
                            print(i.name,"\t",i.enroll,"\t",i.sem,"\t",i.branch,"\t",i.issued_book)
                            f1=1
                            break
                    if(f1==1):
                        break

                except EOFError:
                    print("File is searched, nothing found")
                    break
        else:
            print("There is no such file to search")
            return

# ##########################################-Facualty-##################################################################3

def add_facualty():
        lst2=[]
        obj1=fac.Facualty()
        lst2.append(obj1)
        with open("facualty_record.pkl",'ab') as f:
            pickle.dump(lst2,f)
            print("Facualty Added successfully")

def remove_facualty():
        obj=None
        fl=0
        lt=[]
        while(True):
            print("1>Remove by Facualty Name\n2>Remove By Facualty Id:\n3>Exit")
            inp=int(input())
            if inp==1:
                fm=input("Enter the name of Facualty to eliminate: ")
                with open("facualty_record.pkl",'rb') as f:
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                if i.fname==fm:
                                    fl=1
                                lt.append(i)
                        except EOFError:
                            print("File end")
                            break
                if fl==1:
                    for i in lt:
                        if i.fname==fm:
                            lt.remove(i)

                    with open("facualty_record.pkl",'wb') as f:
                        pass
                    with open("facualty_record.pkl",'ab') as f:
                        pickle.dump(lt,f)
                        print("facualty is eliminated from record")
                        break
              

            if inp==2:
                ide=input("Enter the Facualty Idt No to eliminate facualty:")
                with open("facualty_record.pkl",'rb') as f:
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                if i.fid==ide:
                                    fl=1
                                else:
                                    print("facualty not found")
                                    break
                            lt.append(i)

                        except EOFError:
                            print("File end")
                            break
                if fl==1:
                    for i in lt:
                        if i.fid==ide:
                            lt.remove(i)

                    with open("facualty_record.pkl",'wb') as f:
                        pass
                    with open("facualty_record.pkl",'ab') as f:
                        pickle.dump(lt,f)
                        break
            if inp==3:
                break



def view_all_facualty():
    print("\n****************************Facualty Records***************************")
    with open ("facualty_record.pkl",'rb') as ff:
        if os.path.isfile("facualty_record.pkl")==True:
            print("Facualty Name\tFacualty Id\tIssued Books")
            while(True):
                try:
                    obj=pickle.load(ff)
                    for i in obj:
                        print(i.fname,"\t",i.fid,"\t\t",i.issued_book_facualty)
                except EOFError:
                    print("\nAll Facualty  Displayed\n")
                    return

        else:
            print("No file found")


def view_search_facualty():
    fac=0
    with open("facualty_record.pkl",'rb') as f:
        fkname=input("Enter Name or Facualty Id No to view profile:")
        if os.path.isfile("facualty_record.pkl")==True:
            while(True):
                try:
                    obj=pickle.load(f)
                    for i in obj:
                        if i.fname==fkname or i.fid==fkname:
                            print("Name\tFacualty Id\t\tIssued Books")
                            print(i.fname,"\t",i.fid,"\t\t",i.issued_book_facualty)
                            fac=1
                            break
                    if fac==1:
                        break

                except EOFError:
                    print("File is searched, nothing found")
                    return
        else:
            print("There is no such file to search")
            return

def update_facualty():
        obj=None
        while(True):
            print("1>Update Facualty Name\n2>Update Facualty Id :\n3>Exit")
            inp=int(input())
            if inp==1:
                with open("facualty_record.pkl",'rb') as f:
                    flag=0
                    l=[]
                    bn=input("Enter facualty Name:")
                    while(True):
                        try:
                            obj=pickle.load(f)
                            for i in obj:
                                if bn==i.fname:
                                    flag=1
#                                     i.bname=input("ENTERN NEW NAME")
#                                     l.append(i)
#                                 else:
                                l.append(i)


#                                     i.bname=input("Enter the new name you want to modify")
#                                     print("Name modified successfully")
#                                 else:
#                                     print("No such book found")
#                                     break
                        except EOFError:
#                             print("Updated ucessfully")
                            break
                if(flag==1):
                    for i in l:
                        if bn==i.fname:
                            i.fname=input("Enter New name")
                            break

                    with open("facualty_record.pkl",'wb') as f:
                        pass
                    with open("facualty_record.pkl",'ab') as f:
                        pickle.dump(l,f)
                        print("Updated ucessfully")
            elif inp==2:
                print("🚫Access denied,you can't change Facualty Id")
            elif inp==3:
                break
            else:
                print("Wrong key entered, enter again")
                break
           










































