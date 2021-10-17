''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :6
       o/p=1 2 3 4 5 6
             2 3 4 5 6
               3 4 5 6
                 4 5 6
                   5 6
                     6
'''
def main():#main function to get no. of rows from the user and calling the pattern_e function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_e(n) #calling the function
def pattern_e(n):  #function to print specified pattern

    for i in range(1,n+1):#loop for rows
        for j in range(1,i):#loop that goes till i-1
            print(" ",end=" ") #prints space
        for k in range(i,n+1):#loop for printing the nos. in ith rows
            print(k,end=" ")
        print() #takes control yo next line
        
if __name__ == "__main__":
    main()   #calling main function
