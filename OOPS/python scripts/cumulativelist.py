def main():
    print("enter the no. of elements you want in the list")
    n=int(input()) #to take the no. of elements in the list
    list1=[] 
    for i in range(0,n):
       print("enter the element",i+1,"of the list") #input taken by the user
       list1.append(input()) #appending the list by user input values
    cumulative(list1) #calling the function
def cumulative(list1):
    newlist=[]
    sum1=0
    for i in list1:#for loop to access the items
        sum1=sum1+int(i) #sum for cumulative list
        newlist.append(sum1)#appending the new list
    print("the cumulative list is:",newlist)  
if __name__=="__main__":
    main()
        
        
    