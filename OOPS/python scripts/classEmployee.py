'''
Class 1:
Create a class employee with following attributes:
1. Name
2. EmpID
3. Designation: Worker/ Supervisor/Manager
4. Salary
5. Experience
#Define all getter and setter methods + show method+__str__()
#Calculate Salary according to Designation and experience
#BaseSalary+AddSal+HRA
#BaseSalary is : {10000, 15000, 20000} for Worker, Supervisor, Manager resp
#AddSal=%age experience of BaseSalary 
#HRA=5% of BaseSalary
'''
class Employee:
    #Class Attribute of Employee class
    Salary = {'Worker':10000,'Supervisor':15000,'Manager':20000}
    def __init__(self,Name,Email,Deg,Exp):
        # Constructor for Employee Class
        self.Name = Name
        self.Email= Email
        self.Exp = Exp
        if Deg in Employee.Salary:
            self.Deg = Deg
        else:
            #to raise error if designation is not the one from required
            raise ValueError(f'Mentioned designation: "{Deg}"" is invalid')
    # Getter for Employee properties
    def get_name(self):
        return self.Name
    def get_EmailID(self):
        return self.Email
    def get_designation(self):
        return self.Deg
    def get_experience(self):
        return self.Exp
     
    # Setter for Employee properties
    def set_name(self,name):
        self.name = Name
    def set_EmailID(self,Email):
        self.empID = Email
    def set_designation(self,Deg):
        self.designation = Deg
    def set_experience(self,Exp):
        self.experience = Exp
    #instance method for AddSalary
    def AddSalary(self):
        Addsalary = Employee.Salary[self.Deg] * 0.01*self.Exp + Employee.Salary[self.Deg]
        return f'AddSalary of {self.Deg} is :  {Addsalary}'
    #instance method for HRA
    def HRA(self):
        HRAsalary = Employee.Salary[self.Deg]*0.05
        return f'HRAsalary of {self.Deg} is :  {HRAsalary}'
    #for employee details
    def __str__(self):
        return f"Employee details:\n\nName: {self.Name}\nEmpID: {self.Email}\nDesignation: {self.Deg}\nExperience: {self.Exp}\n{Employee.HRA(self)}\n{Employee.AddSalary(self)}"

#code for input from users

# Name = input('Name of the Employee: ').strip().capitalize()
# Email = input('Email of the Employee: ').strip().capitalize()
# Deg = input('Designation of the Employee: ').strip().capitalize()
# Exp = int(input('Experience of the Employee(integer value): '))
# Employee1 = Employee(Name,Email,Deg,Exp)

#sample input
Employee1 = Employee('Nidhi','N@gmail.com','Manager',3)
print(Employee1)