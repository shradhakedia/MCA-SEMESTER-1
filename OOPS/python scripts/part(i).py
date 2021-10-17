''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :5
       o/p=
* * * * * * * * *
  *           *
    *       *
      *   *
        *
'''
def main():#main function to get no. of rows from the user and calling the pattern_i function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_i(n) #calling the function
def pattern_i(n):#function to print specified pattern
    m = 2*n-1 #assigning m as for n rows we require 2n-1 columns
    for i in range(0,n):#loop for n rows
        for j in range(0,m):#loop for m columns
            if i==0 or i+j==m-1 or i==j:#if condition where * is to be printed in nxm matrix
                print("*",end=" ")
            else:
                print(" ",end=" ") #prints sapce elsewhere
        print()#takes control to next line
        
if __name__ == "__main__":
    main() #calling main function