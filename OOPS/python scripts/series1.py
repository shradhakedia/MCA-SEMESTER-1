'''This program prints the sum of the following series:
    1-x^2/2!+x^4/4!-x^6/6!+...x^n/n!
For Example:i/p=Enter the value upto which sum is to be done : 3
                Enter the value of x : 1
            o/p=0.5402777777777777
'''
import math #importing the maths library

def main(): #main function to take value x and n and call function series1

    n=int(input("Enter the value upto which sum is to be done : "))
    x=int(input("Enter the value of x : "))
    series1(n,x)
    
def series1(n,x): #function to print the sum of series

    sum1=0
    for i in range(0,n+1,1): #for loop from 0 to n
    
        sum1=sum1+(((-1)**i)*(x**(2*i)))/math.factorial(2*i) #calculating the sum
        
    print(sum1)
    
if __name__ == "__main__":
    main() #calling main function
