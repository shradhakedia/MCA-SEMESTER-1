''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :5
       o/p=           5 4 3 2 1 
                      4 3 2 1 
                      3 2 1
                      2 1
                      1
'''
def main():#main function to get no. of rows from the user and calling the pattern_c function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_c(n) #calling the function
def pattern_c(n):  #function to print specified above pattern
    for i in range(n,0,-1):#loop for rows
        for j in range(i,0,-1):#loop for columns
            print(j,end=" ") #prints the no. in (i)th row
        print() #takes the control to next line
        
if __name__ == "__main__":
    main() #calling main function
