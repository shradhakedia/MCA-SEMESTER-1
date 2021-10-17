''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :5
       o/p=        1
                   2 2
                   3 3 3
                   4 4 4 4
                   5 5 5 5 5
'''
def main():#main function to get no. of rows from the user and calling the pattern_d function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_d(n) #calling the function
def pattern_d(n): #function to print specified above pattern
    for i in range(1,n+1): #loop for rows
        for j in range(1,i+1): #loop that goes till i

            print(i,end=" ") #printing i
        print() #takes control to next line
        
if __name__ == "__main__":
    main()   #calling main function 
    


