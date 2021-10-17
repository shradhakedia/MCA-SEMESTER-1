''' 
Define a class Student having 
rollnum, name, marklist, class, Grade, percentage
#constructor
#Accessor (getter)
#Mutators (setter)
#to display complete record of student
#Class var: count no of object
#class set : display count
#Percentage: you've to compute this
#Grade: 
>90, 'A+'
>75, 'A'
>60, 'B+'
>50, 'B'
>40, 'C'
otherwise, 'FAIL'
'''
from class_stack import Stack #importing class stack
class Student:
    count=0 #class variable to count no. of objects
    def __init__(self,arollnum,aname,amarklist,astd="MCA",apercentage=0,agrade="nill"): 
        '''
        constructor:__init__
        parameters:self,arollnum,aname,amarklist,astd="MCA",apercentage=0,agrade="nill"
        '''
        self.rollnum=arollnum
        self.name=aname
        self.marklist=amarklist
        self.std=astd
        self.grade=agrade
        self.percentage=apercentage
        Student.count+=1 #incremention as an instance is made
    def computePercentage(self):
        '''
        function:computePercentage
        parameter:self
        returns: computed percentage
        '''
        self.percentage=sum(self.marklist)//len(self.marklist) 
        return self.percentage
    def computeGrade(self):
        '''
        function:computeGrade
        parameter:self
        returns: computed grade
        '''
        if self.percentage>90: #if percentage is greater than 90
            self.grade="A+"
        elif self.percentage<=90 and self.percentage>75: #else if percentage<=90 and percentage>75:
            self.grade="A"
        elif self.percentage<=75 and self.percentage>60: #else if percentage<=75 and percentage>60:
            self.grade="B+"
        elif self.percentage<=60 and self.percentage>50: #else if percentage<=60 and percentage>50:
            self.grade="B"
        elif self.percentage<=50 and self.percentage>40: #else if percentage<=50 and percentage>40:
            self.grade="C"
        else:
            self.grade="Fail" #else fail
        return self.grade #returning the grade computed
    def get_details(self): 
        #getting the details
        #returns f string, the proper format of the details
        return f"-------- Details of the Student are: -------- \nRollnum:\t{self.rollnum} \nName:\t{self.name} \nStandard:\t{self.std} \nMarksList:\t{self.marklist} \nPercentage:\t{self.computePercentage()} \nGrades:\t{self.computeGrade()}"
    def set_name(self):
        #sets the name
        #returns the name
        self.name=input("Update the name:")
        return self.name
    @classmethod #decorater
    def display_count(cls): #class method 
    #parameter:cls(represents class)
    #returns: class variable count(no. of objects created)
        return cls.count
    def __str__(self):
        #parameter:self
        #pupose:to print the proper format
        #returns: string
        return f"name:{self.name}\nroll num:{self.rollnum}\nStandard:{self.std}\nMarksList:\t{self.marklist} \nPercentage:\t{self.computePercentage()} \nGrades:\t{self.computeGrade()}"
if __name__== "__main__":
    size=int(input(f"Enter the size of the stack:")) #asking for size from the user
    mystack = Stack(size) #creating instance of class Stack
    ch="y" #setting choice as y
    while(ch!="n"):
        #menu for stack
        print("Enter 1 if you want to push the record:")
        print("Enter 2 if you want to see the elements in the stack:")
        print("Enter 3 if you want to pop the record:")
        print("Enter 4 if you want to see the peek record:")
        c=input("Enter your choice:")
        if c=='1': #if c=1
            print(f"--------Enter the details for Student--------")
            try: #exception handling
                rollnum=int(input("Enter the roll number:"))
                name=input("Enter the Name:")
            except:
                print("\t\tWARNING: Roll no. should be an integer and name should be a string.")
            try:
                marklist=list(map(int,input("Enter the Marks for 5 subjects separated by space:").split()))
            except:
                print("\t\t WARNING: Marks should be integer separated by space.")
            stuobj=Student(rollnum,name,marklist) #creating the Student object
            print(stuobj.get_details()) #getting the details
            print(mystack.push(stuobj))#calling push and pushing the object created
            print("---------------stack status-------------")
            for j in mystack.stackList:
                print("-"*20,"\n",j) #print the stack items
        elif c=='2':
            print("No. of elements in stack:",mystack.numOfElements()) #no. of elements
        elif c=='3':
            print("-----Popped element-----\n",mystack.pop()) #popped element
        elif c=='4':
            print("-----Peek element-----\n",mystack.peek()) #peek element
        else:
            print("Wrong choice:") #else wrong choice 
        ch=input("Enter y to continue and n to exit:") #if want to continue or not