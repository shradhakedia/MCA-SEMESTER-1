
def main():
    print("enter the no. of elements you want in the list")
    n=int(input()) #to take the no. of elements in the list
    list1=[]
    for i in range(0,n):
       print("enter the elements of the list one by one") #input taken by the user
       list1.append(input()) #appending the list by the user input value
    remduplicate(list1) #calling the respective function
def remduplicate(list1): #function to remove duplicate items
    newlist=[]
    for items in list1: #loop to check duplicate elements
            if items not in newlist:
                newlist.append(items) #appending the list with non duplicate elements
    print("the new list is :",newlist)
if __name__=="__main__":
    main()
