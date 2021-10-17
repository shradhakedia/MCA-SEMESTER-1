def main():#main function to get no. of rows from the user and calling the pattern_m function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    b=int(input("enter 1 or 0 for your required pattern:"))
    if bool(b)==True:
        pattern_m(n) #calling the function
    else:
        pattern_n(n)
def pattern_m(n):#prints the specified pattern
    p=0 #variable for space printing
    for i in range(n,0,-1):#loop for n rows
        for j in range(0,p):#loop for space
            print(" ",end=" ")
        for k in range(i,0,-1):#loop for printing $ in ith row
            print("$",end=" ")
        p=p+1 #increasing space by 1
        print() #takes control to the next line
def pattern_n(n):#prints the specified pattern
    p=1#variable p for printing #
    for i in range(n,0,-1):#loop for n rows
        for j in range(i-1,0,-1):#loop for space printing
            print(" ",end=" ")
        for k in range(0,p):#loop for printing # in ith row
            print("#",end=" ")
        p=p+1#increasing variable by 1 to print # 
        print()
if __name__ == "__main__":
    main()#calling main function
    