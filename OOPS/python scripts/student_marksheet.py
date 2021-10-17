'''This program performs the following tasks:
1. Create a file containing records of the students marks in each subject. ("studentrecords.txt")
2. Read the file created in step 1, generate the marksheets of individual student and save it in a file named <studentName_rollno>.
3. Also generate a file containing name of students scoring highest marks subject-wise. ("maximum_marks.txt")
'''
import pickle #importing the pickle library

def inputdetails(): 
    '''purpose:To take students details(no. of students,subjects,name,rollno.,marks) as a input from the user and store it in a file("studentrecords") 
       return:students details stored in a dictionary,studentsdetail
       parameters:none
       studentsdetail is created in this format:{'name': ['anjali', 'ankit', 'shradha'], 'rollnum': ['56', '54', '25'], 'oops': ['87', '45', '54'], 'dm': ['74', '14', '78'], 'csa': ['85', '98', '89']}
    '''
    n=int(input("Enter the no. of students:")) #taking no. of students as input
    subjects=input("Enter the subjects separated by space:").strip().split() #taking the subjects and storing it in a list
    studentsdetail={"name":[],"rollnum":[]} #creating a dictionary
    studentsdetail.update({i:[] for i in subjects}) #updating the dictionary with subjects as key and value as a list to store marks of the student
    for i in range(n): #for loop for n no. of students
        for key in studentsdetail: #trascating the keys of studentsdetail dict
            if key in ("name","rollnum"): 
                studentsdetail[key].append(input(f"Enter the {key} of student {i+1}:")) #if key is name or rollnum it appends the keyvalue i.e. list 
            else:
                studentsdetail[key].append(input(f"Enter the {key} marks of student {i+1}:")) #if key is any of the subjects then it appends the keyvalue i.e. list
    return studentsdetail #returns the dictionary

def storedetails(content,mode):
    '''purpose:To store the details in a text file in binary mode 
       return:none
       parameters:content(the dictionary studentsrecord),mode="wb"
    '''
    with open("studentrecords.txt",mode) as f:#create,open and close the file after performing the task
        pickle.dump(content,f) #dumping the content
def readdetails(mode):
    '''purpose:To read the details in a text file in binary mode and create file of each students
       return:none
       parameters:mode="rb"
    '''
    with open("studentrecords.txt",mode) as f: #open and close the file after performing the task
        studentsdetail=pickle.load(f) #loads the dictionary
        for i in range(len(studentsdetail["name"])): #loop for students
            with open(studentsdetail["name"][i]+"_"+studentsdetail["rollnum"][i]+".txt","w") as f1: #creates the file for each student in desired format and write the details
                f1.write("---------------------------MARKSHEET--------------------------\n") #writes this message in file of each student
                for key in studentsdetail: #trascating the keys of dictionary i.e. studentsdetail
                    f1.write(key+"\t\t"+studentsdetail[key][i]+"\n") #writing the details in the file of each student
def maxmarks(mode):
    '''purpose:To read the details in a text file in binary mode and create a file to store maximum marks of each student
       return:none
       parameters:mode="rb"
    '''
    with open("studentrecords.txt",mode) as f: #open and close the file after performing the task
        studentsdetail=pickle.load(f) #loads the dictionary
        with open("maximum_marks.txt","w") as fm: #creates a file for storing maximum marks in each subject
            fm.write("Name\t Subject\t Maximum Marks\n") #writing this message in file
            for key in studentsdetail: #trascating the keys of dictionary i.e. studentsdetail
                if key not in ("name","rollnum"): #if key is subjects and not name and rollnum
                    maximum=max(studentsdetail[key]) #stores the maximum marks of the subject
                    index1=studentsdetail[key].index(maximum) #stores the index of maximum marks of the subject
                    fm.write(studentsdetail["name"][index1]+"\t\t"+key+"\t\t"+maximum+"\n") #writes the name,subject and maximum marks in the file
if __name__ == "__main__":    
    studentsdetail=inputdetails() #calling inputdetails() 
    storedetails(studentsdetail,"wb") #calling storedetails()
    readdetails("rb") #calling read details
    maxmarks("rb") #calling maxmarks