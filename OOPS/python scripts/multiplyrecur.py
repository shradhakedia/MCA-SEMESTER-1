'''The following program writes the function using recursion for Multiplication of two numbers without using multiplication operator.
i/p:Enter first number:15
    Enter second number:6
o/p:The multiplcation is: 90
'''
def multiply(a,b):
    '''Purpose:To multiply the two numbers a,b(given by the user)
       Arguments:a,b
       Return:returns 0 when b=0 else returns the sum of a and the function
    '''
    if b==0: #if condition to check second no. is 0 or not
        return 0 #returns 0 when condition is satified
    else:
        return a + multiply(a,b-1) #recursive call while adding the first no. till second no. of times
if __name__=="__main__":
    m=multiply(int(input("Enter first number:")),int(input("Enter second number:"))) #calling multiply function and storing the returned value in m
    print("The multiplcation is:",m) #print the result