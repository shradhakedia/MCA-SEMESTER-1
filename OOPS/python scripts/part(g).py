''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :5
       o/p=* * * * * 
       	    * * * * *
       	    * * * * * 
       	    * * * * * 
       	    * * * * *
'''
def main():#main function to get no. of rows from the user and calling the pattern_g function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_g(n) #calling the function
def pattern_g(n):
     #function to print specified pattern
     for i in range(0,n):#loop for n rows
         for j in range(0,n):#loop for n columns
             print("*",end=" ")
         print() #takes the control to next line
         
if __name__ == "__main__":
    main()#calling main function
    
     
