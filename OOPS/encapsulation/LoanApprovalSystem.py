class LoanApplication:
    
    def __init__(self):
        print("==== Loan Application System ====")
        self.__income=int
        self.__loanAmount=int
        self.__creditScore=int
        self.__employementYears=int

    def __checkIncome_and_loanAmount(self):
        self.__income=int(input("Enter your Monthly Income: "))
        if self.__income>=40000:
            self.__loanAmount=int(input("Enter your desired Loan Amount: "))
            if self.__loanAmount<=200000:
                return True
            else:
                print("Loan Denied! Loan amount is too high.")
                return False
        else:
            print("Laon Denied! Income is too low.") 
            return False

    def __CreditScoreCheck(self):
        self.__creditScore=int(input("Enter your Credit Score: ")) 
        if self.__creditScore>=700:
            return True
        else:
            print("Your credit score is too low So you are not eligible for Loan.")
            return False

    def __EmployementStatusCheck(self):
        self.__employementYears=int(input("Enter your years of employement: "))
        if self.__employementYears>=2:
            return True
        else:
            print("Your are not eligible for Loan! Applicant must be employed for atleast 2 years.")
            return False
    def LoanApproved(self):  
        if self.__checkIncome_and_loanAmount():
            if self.__CreditScoreCheck():
                if self.__EmployementStatusCheck():
                    print("Congratulations ! Your Loan Approval is approved Successfully.")
                else:
                    print("Loan Denied due to your Employement Status!")
            else:
                print("Loan Denied due to your Credit Score")
        else:
            print("Loan Denied due to Income or Loan Amount!")

                    
ob=LoanApplication()
ob.LoanApproved()


            

 