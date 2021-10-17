''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :5
       o/p=
        *
      *   *
    *       *
  *           *
*               *
  *           *
    *       *
      *   *
        *
'''
def main():#main function to get no. of rows from the user and calling the pattern_k function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_k(n) #calling the function
def pattern_k(n):
    #function to print specified pattern
     m=2*n-1 #for n inputs we need m rows
     for i in range(0,m):#loop for m rows
         for j in range(0,m):#loop for m columns
             if (i+j)==n-1 or (i+j)==n+m-2 or (j-i)==n-1 or (i-j)==n-1:#if condition where * is to be printed in mxm matrices
                 print("*",end=" ")
             else:#else condition where space are to be printed
                 print(" ",end=" ")
         print() #takes control to next line
        
if __name__ == "__main__":
    main() #calling main function
    
    