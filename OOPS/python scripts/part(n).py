''' This program prints the pattern upto (n) nos. input by the user
For eg:i/p=Enter no. of rows :5
       o/p=
        #
      # #
    # # #
  # # # #
# # # # #
'''
def main():#main function to get no. of rows from the user and calling the pattern_n function
    n=int(input("Enter no. of rows :")) #taking the no. of rows
    pattern_n(n) #calling the function
def pattern_n(n):#prints the specified pattern
    p=1#variable p for printing #
    for i in range(n,0,-1):#loop for n rows
        for j in range(i-1,0,-1):#loop for space printing
            print(" ",end=" ")
        for k in range(0,p):#loop for printing # in ith row
            print("#",end=" ")
        p=p+1#increasing variable by 1 to print # 
        print()#takes control to next line
        
if __name__ == "__main__":
    main() #calling main function
