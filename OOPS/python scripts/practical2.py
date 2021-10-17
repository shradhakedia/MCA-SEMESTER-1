'''
The following code creates a class named "Vector" having two components.
The class have the following functions:
1. Subtract two vectors
2. Multiply  two vectors 
 ------------INPUT------------------ 
Enter the ith component for vector1:1
Enter the jth component for vector1:1
Enter the kth component of vector 1:1
Enter the ith component for vector2:2
Enter the jth component for vector2:2
Enter the kth component of vector 1:2
-------------OUTPUT-----------------
The subtraction of vectors: (-1, -1)
The multiplication of vectors: (2, 2, 2)
The no. of vectors object made: 2
'''
#Assumptions:
#A general class of vectors that has two components i and j and k
#two objects are made here, not a user choice
#operations are performed component wise here 
#str is overided to show the input vectors
#components of vectors are shown for vector 1 only due to lack of time
#vector1,vector2 are  the objects(random vectors from R2 space as mentioned two components) of class Vectors
#above output shows clearly everything

class Vectors:
    ''' definition: The class vector has  attributes that are two components of any vector
        contructor: intialize the object's component by given input compnents
        functions: add,subtract,multiply the vectors
    '''
    count=0
    def __init__(self,i,j,k): 
        #contructor to intialize object's(vector) components
        self.i = i
        self.j = j
        self.k = k
        Vectors.count+=1
    
    def __sub__(self,v2):
        '''
        definition: to subtract vectors
        argument: self,  v2(second instance of "Vectors" class)
        return: A tuple i.e the resultant vector
        '''
        _i=self.i - v2.i #subtracting ith component
        _j=self.j - v2.j #subtracting jth component
        _k=self.k - v2.k #subtracting kth component
        return _i,_j,_k #returning the resultant vector as tuple
    def __mul__(self,v2):
        '''
        definition: to multiply vectors
        argument: self,  v2(second instance of "Vectors" class)
        return: A tuple i.e the resultant vector
        '''
        _i=self.i * v2.i #multipling ith component
        _j=self.j * v2.j #multiplying jth component
        _k=self.k * v2.k #multiplying kth component
        return _i,_j,_k #returning the resultant vector as tuple
    @classmethod
    def no_of_objects(cls):
        return cls.count
    def __str__(self):
        return f"The vector you entered is: ({self.i},{self.j},{self.k})"
    def compvector(self):
            ch=input("Enter the 1 to see ith component,2 to see j, and 3 to see kth component:")
            if ch=='1':
                return f"The ith component is: ({self.i})"
            elif ch=='2':
                return f"The jth component is: ({self.j})"
            elif ch=='3':
                return f"The kth component is: ({self.k})"
            else:
                return "Wrong choice."
if __name__=="__main__":
    vector1 = Vectors(int(input("Enter the ith component of vector 1:")),int(input("Enter the jth component of vector 1:")),int(input("Enter the kth component of vector 1:"))) #first instance of Vectors class
    vector2 = Vectors(int(input("Enter the ith component of vector 2:")),int(input("Enter the jth component of vector 2:")),int(input("Enter the kth component of vector 2:"))) #second instance of Vectors class
    print(vector1,vector2)
    print("The subtraction of vectors:",vector1 - vector2)
    print("The multiplication of vectors:",vector1 * vector2)
    print("The no. of vectors object made:",Vectors.no_of_objects())
    choice='y'
    while choice!='n':
        print("Enter 1 to see components of vector1:")
        print("Enter 2 to see components of vector2:")
        n=input("Enter your choice:")
        if n=='1' :
            print(vector1.compvector()) # print the component of first vector
        elif n=='2':
            print(vector2.compvector()) # print the component of second vector
        else:
            print("Wrong choice.")
        choice= input("Enter y to continue and n to exit:")