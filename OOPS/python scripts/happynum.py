'''This program has a function that performs sum of squares of
digits of a number and returns it.Further if the sum is 1 in 10
iterations prints happy number else prints the sum.

Functions: main(),sum_sqd_num()

1) i/p:Enter a number to check happy or not:234
   o/p:The sum is: 58
   
2) i/p:Enter a number to check happy or not:13
   o/p:13 is a happy number
       The sum is: 1
'''

def main():
    '''Purpose: Takes input from the user calls sum_sqd_num,
    stores the sum in sqdNumber_result and check if its 1 prints
    happy or else again calls the function sqdNumber_result to 
    further find the sum of squares of digit.
    Variables:sqdnumber,sqdNumber_result,n
    '''
    sqdnumber=int(input("Enter a number to check happy or not:"))#takes input
    sqdNumber_result=sum_sqd_num(sqdnumber)#calls the respective function
    n=9 #for next 9 iterations
    while(n>0):
        if sqdNumber_result==1:#checks if sum is 1
            print(sqdnumber,"is a happy number")
            break #exits loop as soon as a happy no. is achieved
        else:
            sqdNumber_result=sum_sqd_num(sqdNumber_result)#again calls the function with parameter as the previois sum result 
        n-=1 #updation to while loop
    print("The sum is:",sqdNumber_result)
def sum_sqd_num(sqdnumber):
    ''' Purpose:Finds the sum of square of digits of a no. and returns it
        Parameters:sqdnumber
        Variables:sqdNumber_result,mod
    '''
    sqdNumber_result=0 
    while(sqdnumber>0): #loop to perform sum
        mod=sqdnumber%10 #takes the last digit of the number
        sqdNumber_result+=mod**2 #adds the sqaure of the digit in sqdNumber_result
        sqdnumber//=10 #divides the number bu 10
    return sqdNumber_result #returns the final result
    
if __name__=="__main__": 
    main() #calling main function
