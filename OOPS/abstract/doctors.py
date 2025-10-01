from abc import ABC,abstractmethod

class Doctor(ABC):

    @abstractmethod
    def specialization(self):
        pass

    @abstractmethod
    def provide_treatment(self):
        pass
 
class Cardiologist(Doctor):
    
    def specialization(self):
        print("Specialization:- Heart Specialist")

    def provide_treatment(self):
        print("Treat patients of heart-related issues.")

class Neurologist(Doctor):

    def specialization(self):
        print("Specialization:- Brain Specialist")   

    def provide_treatment(self):
        print("Treat patients of neurological disorder.")    

ob=Neurologist()
ob.specialization()
ob.treatment()
 
