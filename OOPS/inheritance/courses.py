class Courses():

    def Student(self):
        print("Courses Information for Students:- ")
    def Attendance(self):
        print("Attendance:- The attendance of every student must be 75%.")  
    def FeesStructure(self):
        print("Fees:- Annual")      

class BSc(Courses):
    
    def duration(self):
        print("Duration:- 3 years")
    def courses(self):
        print("Subjects:- Physics, Chemistry, Math, etc.")
    def careerOptions(self):
        print("CarrerOptions:- Research, Higher Studies, Teaching") 

class BTech(Courses):
    
    def duration(self):
        print("Duration:- 4 years")
    def courses(self):
        print("Subjects:- Structural Analysis, Digital Electronics etc.")
    def careerOptions(self):
        print("CarrerOptions:- Software Engineer, Civil Engineer, Electrical Engineer")

class BCA(Courses):
    
    def duration(self):
        print("Duration:- 3 years") 
    def courses(self):
        print("Subjects:- Web Development, DBMS, OOPS, Software Engineering etc.")
    def careerOptions(self):
        print("CarrerOptions:- Software Developer, Web Developer")

class LLB(Courses):
    
    def duration(self):
        print("Duration:- 5 years")
    def courses(self):
        print("Subjects:- Constitutional Law, Criminal Law etc.")
    def careerOptions(self):
        print("CarrerOptions:- Lawyer, Judge")

class BEd(Courses):

    def duration(self):
        print("Duration:- 2 years")
    def courses(self):
        print("Subjects:- Educational Psychology, Teaching Methodology etc.")
    def careerOptions(self):
        print("CarrerOptions:- Teaching (Primary, Secondary, Senior Secondary Level)")

class MBA():
    
    def duration(self):
        print("Duration:- 2 years")
    def courses(self):
        print("Subjects:- Strategic Management, Business Analytics")
    def careerOptions(self):
        print("CarrerOptions:- Business Analyst, Project Manager")

class ViewAllCourses():
    
    def show_all_courses(self):
        print("\n========= Viewing All Courses Information =========\n")

        courses_dicdata = {"bsc":BSc, 
                           "btech":BTech, 
                           "bca":BCA, 
                           "llb":LLB, 
                           "bed":BEd, 
                           "mba":MBA
    }

        bsccourse=courses_dicdata["bsc"]()
        bsccourse.duration()
        bsccourse.courses()
        bsccourse.careerOptions()

        btechcourse=courses_dicdata["btech"]()
        btechcourse.duration()
        btechcourse.courses()
        btechcourse.careerOptions()

        bcacourse=courses_dicdata["bca"]()
        bcacourse.duration()
        bcacourse.courses()
        bcacourse.careerOptions()

        llbcourse=courses_dicdata["llb"]()
        llbcourse.duration()
        llbcourse.courses()
        llbcourse.careerOptions()

        bedcourse=courses_dicdata["bed"]()
        bedcourse.duration()
        bedcourse.courses()
        bedcourse.careerOptions()

        mbacourse=courses_dicdata["mba"]()
        mbacourse.duration()
        mbacourse.courses()
        mbacourse.careerOptions()



