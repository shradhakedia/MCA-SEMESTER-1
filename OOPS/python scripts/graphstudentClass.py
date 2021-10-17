#from graphstudentClass import Student
class Student:
    count=0
    def __init__(self,arollnum,aname,amarklist,astd="MCA",apercentage=0,agrade="nill"):
        self.rollnum=arollnum
        self.name=aname
        self.marklist=amarklist
        self.std=astd
        self.grade=agrade
        self.percentage=apercentage
        Student.count+=1
    def computePercentage(self):
        self.percentage=sum(self.marklist)//len(self.marklist)
        return self.percentage
    def computeGrade(self):
        if self.percentage>90:
            self.grade="A+"
        elif self.percentage<=90 and self.percentage>75:
            self.grade="A"
        elif self.percentage<=75 and self.percentage>60:
            self.grade="B+"
        elif self.percentage<=60 and self.percentage>50:
            self.grade="B"
        elif self.percentage<=50 and self.percentage>40:
            self.grade="C"
        else:
            self.grade="Fail"
        return self.grade
    def get_details(self):
        return f"-------- Details of the Student are: -------- \nRollnum:\t{self.rollnum} \nName:\t{self.name} \nStandard:\t{self.std} \nMarksList:\t{self.marklist} \nPercentage:\t{self.computePercentage()} \nGrades:\t{self.computeGrade()}"
    def set_name(self):
        self.name=input("Update the name:")
        return self.name
    @classmethod
    def display_count(cls):
        return cls.count
    def __str__(self):
            return f"name:{self.name}\nroll num:{self.rollnum}\nStandard:{self.std}\nMarksList:\t{self.marklist} \nPercentage:\t{self.computePercentage()} \nGrades:\t{self.computeGrade()}"
if __name__== "__main__":
    studentlist=[]
    ch='y'
    while ch!='n':
        print(f"--------Enter the details for Student--------")
        rollnum=int(input("Enter the roll number:"))
        name=input("Enter the Name:")
        marklist=list(map(int,input("Enter the Marks for 5 subjects separated by space:").split()))
        studentlist.append(Student(rollnum,name,marklist))
        ch=input("Enter your choice y/n if you want more student records:")
    count=Student.display_count()
    print("The number of objects created are:",count)
    for i in range(count):
        print(studentlist[i].get_details())
    choice=input("You can update the name if you want! \nEnter(y/n):")
    while choice=="y":
        stuchoice=input("Enter 1 to update student 1 name or 2 for student 2 and so on...")
        studentlist[int(stuchoice)-1].set_name()
        print(studentlist[int(stuchoice)-1].__dict__)
        choice=input("Enter y to continue and n to exit:")
    
    