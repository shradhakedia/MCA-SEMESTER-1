''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :5
       o/p=$ $ $ $ $
             $ $ $ $
               $ $ $
                 $ $
                   $
'''
def main():#main function to get no. of rows from the user and calling the pattern_m function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_m(n) #calling the function
def pattern_m(n):#prints the specified pattern
    p=0 #variable for space printing
    for i in range(n,0,-1):#loop for n rows
        for j in range(0,p):#loop for space
            print(" ",end=" ")
        for k in range(i,0,-1):#loop for printing $ in ith row
            print("$",end=" ")
        p=p+1 #increasing space by 1
        print() #takes control to the next line

if __name__ == "__main__":
    main()#calling main function
    
     