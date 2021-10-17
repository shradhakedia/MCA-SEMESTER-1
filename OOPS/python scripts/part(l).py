''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :5
       o/p=
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
def main():#main function to get no. of rows from the user and calling the pattern_l function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_l(n) #calling the function
def pattern_l(n):
    #function to print specified pattern
    for i in range(1,2*n,1):
        if i<=n:#for upper half traingle
            for j in range(n-i,0,-1):#loop for space
                print(" ",end=" ")
            for j in range(0,i):#loop for upper left triangle
                print("*",end=" ")
            for j in range(1,i):#loop for upper right triangle
                print("*",end=" ")
            print( )
        else:#lower half triangle
            for j in range(1,i-n+1,1):#loop for space
                print(" ",end=" ")
            for j in range(2*n-i,0,-1):#loop for lower left triangle
                print("*",end=" ")
            for j in range(2*n-i-1,0,-1):#loop for lower right triangle
                print("*",end=" ")
            print()#takes control to next line
if __name__ == "__main__":
    main()#for calling main function
    
    
    