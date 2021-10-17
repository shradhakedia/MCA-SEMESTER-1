'''This program takes a input n and m from the user
and then n inputs for the list and 
further checks which pairs sum to m
For Example:
Enter n:5
Enter the list elements
10
30
8
23
1
[10, 30, 8, 23, 1]
Enter m:31
The pairs are:
( 30 , 1 )
( 8 , 23 )
'''
def main():#main function that takes m,n,and n elements for list and calls functiom sums
    n=int(input("Enter n:"))
    list1=[] #empty list 
    print("Enter the list elements")
    for i in range(1,n+1): #loop to take n inputs
        list1.append(int(input())) #appends the list with the input values
    print(list1) #prints the list1
    m=int(input("Enter m:")) #takes input m
    print("The pairs are:") 
    sums(m,list1) #calls function sums
def sums(m,list1):#this function returns nothing but prints the pairs that sum to m
    for i in range(0,len(list1)): #loop for taking elements one by one
        for j in range(i+1,len(list1)):#loop for taking elements further i
            list2=[]
            if m==list1[i]+list1[j]:#checks if pairs sum to m
                list2.append(list1[i])
                list2.append(list2[j])
                print(list2)
                print("(",list1[i],",",list1[j],")")
            
if __name__=="__main__":
    main() #calling main function
    
