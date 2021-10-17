''' This program takes a input n from the user upto which primes and 
no. of primes are to be printed.
For Example:
Enter the no. upto which you want to find primes: 21
prime nos. upto n are:
2
3
5
7
11
13
17
19
number of primes upto n are 8
'''
def main(): #this main function takes the input n from the user and prints the primes ans nos. of primes upto n
    n=int(input("Enter the no. upto which you want to find primes: "))
    count=0 #local variable to count the prime nos 
    print("prime nos. upto n are:")
    for num in range(2,n+1): #loop from 2 to n to check which are primes in it
        s=primes(num) #calling primes function
        if s==1: #returns 1 if num is prime
            count+=1
            print(num) #prints the prime
    print("number of primes upto n are",count) #prints the no. of primes
def primes(num): # this function returns 1 when num is prime else returns 0
    flag=0 #flag variable
    for i in range(1,num+1): #loop to count the divisors of num
        if num%i==0: #checks if i is divisor of num
            flag+=1 #counts the divisors of num
    if flag==2: #checks if the no. of divisors upto num are only 2 or not
        return 1 #returns 1 if codition is satisfied
    else:
        return 0 #returns 0 when num is non prime
if __name__=="__main__":
    main() #calling main function
