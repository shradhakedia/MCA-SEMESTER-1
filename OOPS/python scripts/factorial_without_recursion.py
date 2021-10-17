'''The Program takes input x from a user and
prints the factorial from 1 to x
For Example: i/p:Enter a number greater than 0:6
o/p:The factorial of 1 is 1
    The factorial of 2 is 2
    The factorial of 3 is 6
    The factorial of 4 is 24
    The factorial of 5 is 120
    The factorial of 6 is 720
    The factorial of 7 is 5040
'''
def main(): 
    '''Purpose:The main function returns takes input from the user
          and calls the function fact() with parameter x
       Variable:x,Arguments:x
    '''
    x=int(input("Enter a number greater than 0:")) #taking input from the user
    fact(x) #calling the functiom
def fact(x):
    '''Purpose:The fact function find the factorial of numbers till x
       Parameters:x
       Variables:factorial,i
    '''
    factorial=1 
    for i in range(x): #for iteration upto x
        factorial=factorial*(i+1) #multiplying til the iteration continues
        print(f"The factorial of {i+1} is {factorial}") #prints factorial of each no. till x
if __name__=="__main__":
    main() #calling main function
