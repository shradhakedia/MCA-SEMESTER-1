def main():#to take the input from the user and calling the multiple list function
    print("enter the value of n")
    n=int(input()) #to take input as the dimension list
    list_multiples(n) 
def list_multiples(n):#function that returns the appended list with its multiples upto 5
    list1=[]
    for i in range(1,n+1): #loop to access the outer dimension of the list
        a=[i*k for k in range(1,6)] #using list comprehension to take the multioles upto 5
        list1.append(a) #appending the list with the multiple list
    print(list1)
if __name__=="__main__":
    main()
