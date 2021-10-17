''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :5
       o/p=
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
def main():#main function to get no. of rows from the user and calling the pattern_j function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_j(n) #calling the function
def pattern_j(n):#function to print specified pattern
    for i in range(0,n):#loop for n rows
        for j in range(0,i):#loop for space
            print(" ",end=" ")
        for k in range(n-i,0,-1):#loop for * in right triangle
            print("*",end=" ")
        for l in range(n-i-1,0,-1):#loop for * in left triangle
            print("*",end=" ")
        print() #takes control to next line
if __name__ == "__main__":
    main() #calling main function