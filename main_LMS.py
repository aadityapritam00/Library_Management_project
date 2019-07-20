import getpass
import os,sys
import time
from functionality import *
import student as std 
import  book as bkk
import facualty as facl
# import welcomeAdmin as wa
# import Student_welcome as ws
import loading as ld
import load as lo

def main():
    print("***********************************📚LIBRARY MANAGEMENT SYSTEM📝**************************************")
    while True:
        print("\n1>Student LogIn\t\t2>Facualty LogIn\n3>Admin LogIn\t\t4>Exit")
        inp=int(input())
        if inp==1:
            sid=input("Syudent Id:")
            spassword=getpass.getpass(prompt="Password👁‍🗨")
#             while(True):
            if spassword=='sistec0187':
                time.sleep(2)
                ld.loading_view()
#                 ws.StudentWelcome()
#                 ws.StudentWelcome()
                print("Log In successfully✅")
                print("=====================================STUDENT DASHBOARD======================================")
                while(True):
                    print("1>Show All Books\t2>Search Book\t3>Request Book\t\t4>View Profile\t\t5>Exit")
                    inp1=int(input())
                    if inp1==1:
                        show_all_book()
                    elif inp1==2:
                        search_book()
                    elif inp1==3:
                        request_book()
                    elif inp1==4:
                        view_search_student()
                    elif inp1==5:
                        break
                    else:
                        print("Wrong key entered")
                        

            else:
                print("❌Incorect Pin,Try again")
                break
            
        elif inp==2:
            fid=input("Techer Id:")
            fpassword=getpass.getpass("Password👁‍🗨")
            if fpassword=='sistec0187':
                print("please wait.........")
                time.sleep(2)
                ld.loading_view()
                print("\n✅LogIn Successfully")
                while (True):
                    print("1>View All Books\t2>Request Book\t3>Search Book\t4>View Your Profile\t5>Back\t6>Exit")
                    inp1=int(input())
                    if inp1==1:
                        show_all_book()
                    elif inp1==2:
                        request_book()
                    elif inp1==3:    
                        search_book()
                    elif inp1==4:
                        view_search_facualty()
                    elif inp1==5:
                        return 
                    elif inp1==6:
                        sys.exit()
                    else:
                        print("🔒Incorrect key entered❌,try again")
                        return
                    
            else:
                print("Incorrect Password❌")
                break
                    
        elif inp==3:
            aid=input("Admin Id:")
            fpassword=getpass.getpass("Password🔑🔒")
            if fpassword=='sistec0187':
                time.sleep(2)
                lo.Load()
                print("✅LogIn Successfully")
                print("------------------------------Admin Dashboard-------------------------------")
#                 wa.Admin_welcome()
                print("Welcome Admin !")
                while(True):
                    print("please specify To work on\n1>Books\n2>Student\n3>Facualty\n4>Exit")
                    inp2=int(input())
                    if inp2==1:
                        while(True):
                            print("1>Add Book\t2>view All book\n3>Remove Book\t4>Search Book\n5>Update Book\t6>Back\t7>Exit")
                            inp3=int(input())
                            if inp3==1:
                                add_book()
                            elif inp3==2:
                                show_all_book()
                            elif inp3==3:
                                remove_book()
                            elif inp3==4:
                                search_book()
                            elif inp3==5:
                                modify_book()
                            elif inp3==6:
                                return
                            elif inp3==7:
                                break
                            else:
                                print("wrong key entered, try again !")
                                return

                    elif inp2==2:
                        while(True):
                            print("1>View students record\t2>Add student\t3>Search student \t4>Remove student \t5>Update Student\n6>Back\t7>Exit")
                            inp3=int(input())
                            if inp3==1:
                                view_all_student()
                            elif inp3==2:
                                add_student()
                            elif inp3==3:    
                                view_search_student()
                            elif inp3==4:
                                eliminate_student()
                            elif inp3==5:
                                update_student()
                            elif inp3==6:
                                break
                            elif inp==7:
                                sys.exit()
                            else:
                                print("Incorrect key entered❌,try again")
                                return

                    elif inp2==3:
                        print("1>View Facualty records\t2>Add New Facualty\n3>Search Facualty\t4>Remove Facualty\n5>Update Facualty\t6>Back\n7>Exit")
                        inp3=int(input())
                        if inp3==1:
                            view_all_facualty()
                        elif inp3==2:
                            add_facualty()
                        elif inp3==3:    
                            view_search_facualty()
                        elif inp3==4:
                            remove_facualty()
                        elif inp3==5:
                            update_facualty()
                        elif inp3==6:
                            return
                        elif inp3==7:
                            sys.exit()
                        else:
                            print("Incorrect key entered❌,try again")
                            
                        
                    elif inp2==4:
                        sys.exit()
                    
            else:
                print("🔒Incorrect Password❌,try again")
                return
        
        elif inp==4:
            break
            
        else:
            print("wrong key entered, please try again ")
            break
                    
            
main()