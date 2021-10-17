'''
(1):marksList.append(int(m1)) #Statement 1
(2):if i>100 or i<0: #Statement 2
(3):if validateMarks(marks1)==False or validateMarks(marks2)==False: #statement 3
(4):for i in range(numStudent): #statement 4
(5):TotalMarks.append(marks1[i]+marks2[i]) #statement 5
'''
#Function to take input marks of students in list ‘marksList’ with total strength ‘numStudent’
def inputMarks(numStudent):
    marksList=list()
    for i in range(numStudent):
        m1=input("Enter marks for student "+str(i+1)+":")
        marksList.append(int(m1)) #Statement 1
    return marksList
#Function to validate the input marks i.e. marks should be between 0 to 100.
#returns TRUE if list of marks is valid otherwise returns FALSE
def validateMarks(marks):
    for i in marks:
        # Traverse each element 
        if i>100 or i<0: #Statement 2
            return False
        return True
#Main Script
def main():
    TotalMarks=[]
    numStudent=int(input("Enter Total Number of students:"))
    print("Enter Marks for 1st subject")
    marks1=inputMarks(numStudent)
    print("Enter Marks for 2nd subject")
    marks2=inputMarks(numStudent)
    if validateMarks(marks1)==False or validateMarks(marks2)==False: #statement 3
        print("Invalid Marks")
    else:
        for i in range(numStudent): #statement 4
            TotalMarks.append(marks1[i]+marks2[i]) #statement 5
    print(TotalMarks)
main()