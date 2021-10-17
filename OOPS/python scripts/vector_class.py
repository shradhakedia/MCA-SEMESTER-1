'''
The following code creates a class named "Vector" having two components.
The class have the following functions:
1. Add two vectors
2. Subtract two vectors
3. Multiply  two vectors 
 ------------INPUT------------------ 
Enter the ith component for vector1:1
Enter the jth component for vector1:2
Enter the ith component for vector2:3
Enter the jth component for vector2:1
-------------OUTPUT-----------------
The addition of vectors: (4, 3)
The subtraction of vectors: (-2, 1)
The multiplication of vectors: (3, 2)
'''
#Assumptions:
#A general class of vectors that has two components i and j
#operations are performed component wise here 
#vector1,vector2 are just the objects(random vectors from R2 space as mentioned two components) of class Vectors
#above output shows clearly everything

class Vectors:
    ''' definition: The class vector has  attributes that are two components of any vector
        contructor: intialize the object's component by given input compnents
        functions: add,subtract,multiply the vectors
    '''
    def __init__(self,i,j): 
        #contructor to intialize object's(vector) components
        self.i = i
        self.j = j
    def __add__(self,v2):
        '''
        definition: to add vectors
        argument: self,  v2(second instance of "Vectors" class)
        return: A tuple i.e the resultant vector
        '''
        _i=self.i + v2.i #adding ith component
        _j=self.j + v2.j #adding jth component
        return _i,_j #returning the resultant vector as tuple
    def __sub__(self,v2):
        '''
        definition: to subtract vectors
        argument: self,  v2(second instance of "Vectors" class)
        return: A tuple i.e the resultant vector
        '''
        _i=self.i - v2.i #subtracting ith component
        _j=self.j - v2.j #subtracting jth component
        return _i,_j #returning the resultant vector as tuple
    def __mul__(self,v2):
        '''
        definition: to multiply vectors
        argument: self,  v2(second instance of "Vectors" class)
        return: A tuple i.e the resultant vector
        '''
        _i=self.i * v2.i #multipling ith component
        _j=self.j * v2.j #multiplying jth component
        return _i,_j #returning the resultant vector as tuple
    def __str__(self):
        return f"The vector is: ({self.i},{self.j})"
if __name__=="__main__":
    vector1 = Vectors(int(input("Enter the ith component of vector 1:")),int(input("Enter the jth component of vector 1:"))) #first instance of Vectors class
    vector2 = Vectors(int(input("Enter the ith component of vector 2:")),int(input("Enter the jth component of vector 2:"))) #second instance of Vectors class
    print(vector1,vector2)
    print("The addition of vectors:",vector1 + vector2)
    print("The subtraction of vectors:",vector1 - vector2)
    print("The multiplication of vectors:",vector1 * vector2)
    