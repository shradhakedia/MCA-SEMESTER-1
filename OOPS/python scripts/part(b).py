''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :4
       o/p=            1
                     2 1 2
                   3 2 1 2 3
                 4 3 2 1 2 3 4
'''


def main():#main function to get no. of rows from the user and calling the pattern_b function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_b(n) #calling the function 

def pattern_b(n):  #function to print specified above pattern
    p=n-1 #variable taken to print the spaces
    for i in range(1,n+1): #loop for rows
        for j in range(p,0,-1): #loop for printing spaces in columns
            print(" ",end=" ")
        for k in range(i+1,1,-1): #loop for printing nos. in columns
            print(k-1,end=" ")
        for l in range(1,i): #for further nos. 
            print(l+1,end=" ")
        p=p-1 #decreasing the space by one
        print() #takes the control to next line

if __name__ == "__main__":
    main() #calling main function