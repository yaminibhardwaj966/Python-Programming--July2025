from inheritance.courses import Courses
from inheritance.courses import BSc
from inheritance.courses import BTech
from inheritance.courses import BCA
from inheritance.courses import LLB
from inheritance.courses import BEd
from inheritance.courses import MBA
from inheritance.courses import ViewAllCourses
import time

while(True):
    print("\n------- Search Specific Course Details -------")
    print("Press 1 for view Bsc Course Details.")
    print("Press 2 for view BTech Course Details.")
    print("Press 3 for view BCA Course Details.")
    print("Press 4 for view LLB Course Details.")
    print("Press 5 for view BEd Course Details.")
    print("Press 6 for view MBA Course Details.")
    print("Press 7 for View All Courses Details.")
    print("Press 0 for exit.")

    try:
        choice=int(input("Please enter any choice: "))
    except ValueError:
        print("Please enter only integers!")

    if choice==1:
        print("\n==== BSc Course Details ====\n")
        ob=BSc()
        ob.Student()
        ob.Attendance()
        ob.FeesStructure()
        ob.duration()
        ob.courses()
        ob.careerOptions() 
        
    elif choice==2:
        print("\n==== BTech Course Details ====\n")
        ob=BTech()
        ob.Student()
        ob.Attendance()
        ob.FeesStructure()
        ob.duration()
        ob.courses()
        ob.careerOptions()
        
    elif choice==3:
        print("\n==== BCA Course Details =====\n")
        ob=BCA()
        ob.Student()
        ob.Attendance()
        ob.FeesStructure()
        ob.duration()
        ob.courses()
        ob.careerOptions() 
        
    elif choice==4:
        print("\n==== LLB Course Details ====\n")
        ob=LLB()
        ob.Student()
        ob.Attendance()
        ob.FeesStructure()
        ob.duration()
        ob.courses()
        ob.careerOptions() 
        
    elif choice==5:
        print("\n==== BEd Course Details ====\n")
        ob=BEd()
        ob.Student()
        ob.Attendance()
        ob.FeesStructure()
        ob.duration()
        ob.courses()
        ob.careerOptions()        
            
    elif choice==6:
        print("\n==== MBA Course Details ====\n")
        ob=MBA()
        ob.Student()
        ob.Attendance()
        ob.FeesStructure()
        ob.duration()
        ob.courses()
        ob.careerOptions() 
        
    elif choice==7:
        ob=ViewAllCourses()
        ob.show_all_courses()

    elif choice==0:
        print("Exiting.....")
        time.sleep(2)
        print("Thank u for visiting.")
        break
        
    else:
        print("Please choose correct option!")    