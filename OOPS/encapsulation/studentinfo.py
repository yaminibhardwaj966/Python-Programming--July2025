class Student:

    def __init__(self):
        print("---- Student Registration ----")
        self.id=int(input("Please enter student Id: "))
        self.name=input("Please enter student Name: ")
        self.address=input("Please enter student Address: ")

    def Menu(self):
        print("==== MENU ====")    
        print("Press 1 for Display Student Records.")
        print("Press 2 for Update Student Records.")
        option=int(input("Please enter your choice: "))
        if option==1:
            self.ViewStudentRecord()
        elif option==2:
            self.UpdateStudentRecord()
        else:
            print("Please enter correct Option!")        

    def ViewStudentRecord(self):
        print(f"ID: {self.id} | Name: {self.name} | Address: {self.address}")

    def UpdateStudentRecord(self):
        print("---- Updation Menu ----")
        print("Press 1 for update student name.")
        print("Press 2 for update student address.")
        choice=int(input("Please enter your choice: "))        
        if choice==1:
            newname=input("Please enter Name: ")
            self.name=newname
        elif choice==2:
            newaddress=input("Please enter Address: ")
            self.address=newaddress
        else:
            print("Please enter correct option!")

ob=Student()
ob.Menu()

           
