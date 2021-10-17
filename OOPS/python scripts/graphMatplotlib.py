import numpy
import matplotlib.pyplot as plt 
def inputdetails(n): 
    '''purpose:To take students details(no. of students,subjects,name,rollno.,marks) as a input from the user and store it in a file("studentrecords")        return:students details stored in a dictionary,studentsdetail
       parameters:none
       studentsdetail is created in this format:{'name': ['anjali', 'ankit', 'shradha'], 'oops': ['87', '45', '54'], 'dm': ['74', '14', '78'], 'csa': ['85', '98', '89']}
    '''
    studentsdetail={"name":[],"Oops":[],"CSA":[],"DM":[],"MathTech":[],"TechComm.":[]} #creating a dictionary
    for i in range(n): #for loop for n no. of students
        for key in studentsdetail: #trascating the keys of studentsdetail dict
            if key=="name": 
                studentsdetail[key].append(input(f"Enter the {key} of student {i+1}:")) #if key is name or rollnum it appends the keyvalue i.e. list 
            else:
                studentsdetail[key].append(int(input(f"Enter the {key} marks of student {i+1}:"))) #if key is any of the subjects then it appends the keyvalue i.e. list
    return studentsdetail #returns the dictionary
def stuplot(n,studentsdetail):
    for i in range(n):
        plt.subplot(n,1,i+1)
        xplot=["Oops","CSA","DM","Mathtech","Techcomm."]
        yplot=[studentsdetail["Oops"][i],studentsdetail["CSA"][i],studentsdetail["DM"][i],studentsdetail["MathTech"][i],studentsdetail["TechComm."][i]]
        plt.plot(xplot,yplot)
        plt.title(studentsdetail["name"][i])
    plt.show()
def stupieplot(n,studentsdetail):
    for i in range(n):
        plt.subplot(n,1,i+1)
        yplot=[studentsdetail["Oops"][i],studentsdetail["CSA"][i],studentsdetail["DM"][i],studentsdetail["MathTech"][i],studentsdetail["TechComm."][i]]
        mylabels=["oops","csa","dm","mtcs","tc"]
        y=[]
        for j in yplot:
            y.append(j/sum(yplot))
        plt.pie(y,labels = mylabels)
        plt.legend(title="Subject name:")
        plt.title(studentsdetail["name"][i])
    plt.show()
def subbarplot(n,studentsdetail):
    plt.subplot(5,1,1)
    x=["student"+str(i+1) for i in range(n)]
    plt.bar(x,studentsdetail["Oops"])
    plt.title("Oops record")
    plt.subplot(5,1,2)
    x=["student"+str(i+1) for i in range(n)]
    plt.bar(x,studentsdetail["CSA"])
    plt.title("CSA record")
    plt.subplot(5,1,3)
    x=["student"+str(i+1) for i in range(n)]
    plt.bar(x,studentsdetail["DM"])
    plt.title("DM record")
    plt.subplot(5,1,4)
    x=["student"+str(i+1) for i in range(n)]
    plt.bar(x,studentsdetail["MathTech"])
    plt.title("MathTech record")
    plt.subplot(5,1,5)
    x=["student"+str(i+1) for i in range(n)]
    plt.bar(x,studentsdetail["TechComm."])
    plt.title("TechComm. record")
    plt.show()
if __name__=="__main__":
    n = int(input("Enter the no. of students:")) #taking no. of students as input
    studentsdetail=inputdetails(n)
    print(studentsdetail)
    t="y"
    while t=="y":
        print("Enter 1 to see marks graph for all the students respectively")
        print("Enter 2 to see pie chart for all the students respectively")
        print("Enter 3 to see bar graph for all the subjects respectively")
        ch=int(input("Enter your choice:"))
        if ch==1:
            stuplot(n,studentsdetail)
        elif ch==2:
            stupieplot(n,studentsdetail)
        elif ch==3:
            subbarplot(n,studentsdetail) 
        else:
            print("Wrong choice")
        t=input("Enter n to exit y to continue:")
            