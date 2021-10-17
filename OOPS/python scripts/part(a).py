''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :5
       o/p=1
           1 2
           1 2 3
           1 2 3 4
           1 2 3 4 5
'''
def main(): #main function to get no. of rows from the user and calling the pattern_a function
    n=int(input("Enter no. of rows :")) #taking input n
    pattern_a(n)#calling this function

def pattern_a(n): #function to print specified above pattern
    for i in range(1,n+1): #loop for rows
        for j in range(1,i+1): #loop for coloumns
            print(j,end=" ") #printing the nos. in (i)th rows 
        print() #taking the control to next line

if __name__ == "__main__":
    main() #calling the main function
