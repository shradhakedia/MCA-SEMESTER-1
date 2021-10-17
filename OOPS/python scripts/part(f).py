''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :5
       o/p=* * * * * 
       	    *       * 
       	    *       *
       	    *       *
       	    * * * * *
'''
def main():#main function to get no. of rows from the user and calling the pattern_f function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_f(n) #calling the function
def pattern_f(n):  #function to print specified pattern
    for i in range(0,n):#loop for n rows
        for j in range(0,n):#loop for n columns
            if (i==0 or i==n-1 or j==0 or j==n-1):#conditions where we want to print *
                print("*",end=" ")
            else:#for printing space
                print(" ",end=" ")
        print()#to take the control to next line
        
if __name__ == "__main__":
    main()#calling main function
