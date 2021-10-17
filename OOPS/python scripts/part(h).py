''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :4
       o/p=        *
                 * * *
               * * * * *
             * * * * * * *
'''
def main():#main function to get no. of rows from the user and calling the pattern_h function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_h(n) #calling the function
def pattern_h(n):
    #function to print specified pattern
    for i in range(1,n+1):#loop for n rows
        for j in range(n-i,0,-1):#loop for printing space
            print(" ",end=" ")
        for k in range(0,i):#loop for printing * in left side traingle
            print("*",end=" ")
        for l in range(1,i):#loop for printing * in right side triangle
            print("*",end=" ")
        print() #takes control to next line

if __name__ == "__main__":
    main() #calling main function
