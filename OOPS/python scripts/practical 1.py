'''Define a function which takes two arguments:
n: number of rows
patternType: Type of pyramid to print,
1: Right angle triangle of squares of numbers with n rows
Example:
n = 3
Right angle triangle is

1
4 9
16 25 36

2: Right angle triangle with n rows as:
n=5

Output

1
22
333
4444
55555
'''
def pattern(n,choice):
    if choice=='1':
        k=1
        for i in range(n+1):
            for j in range(i):
                print(k**2,end=" ")
                k+=1
            print()
    elif choice=='2':
        for i in range(1,n+1): #loop for rows
            for j in range(1,i+1): #loop that goes till i
                print(i,end=" ") #printing i
            print() #takes control to next line
    else:
            print("wrong choice")
if __name__=="__main__":
    ch='y'
    while ch!='n':
        n,choice=map(str,input("Enter the no. of rows and choice of triangle, you wish to see, separated by space:").split())
        pattern(int(n),choice)
        ch=input("Enter n to exit y to continue:")
