'''This program takes a input n from the user
and prints the list of even and odd numbers upto n 
For Example:
Enter the value of n upto which evens and odds are to be printed:15
the list of odd nos. is: [1, 3, 5, 7, 9, 11, 13, 15]
the list of even nos. is: [2, 4, 6, 8, 10, 12, 14]
'''
def main(): #this function takes input from the user and calls oddeven() function
    n=int(input("Enter the value of n upto which evens and odds are to be printed:"))
    oddeven(n) #calling the function
def oddeven(n): #this function returns nothing but prints the odd and even nos. list upto n 
    odd,even=[],[] #null lists 
    for i in range(1,n+1): #loop from 1 to n to check even and odds
        if i%2==0: #if condition that checks even
            even.append(i) #appends the list even with even nos.
        else:
            odd.append(i) #appends the list odd with odd nos.
    print("the list of odd nos. is:",odd) #prints the list odd
    print("the list of even nos. is:",even) #print the even list
if __name__=="__main__":
    main() #calling main function
