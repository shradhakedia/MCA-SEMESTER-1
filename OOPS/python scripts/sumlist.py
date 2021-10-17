'''The following program takes two list memebers separated by
commas and prints the sum of the corresponding elements
if their length is same or just returns the element as it is
if there is no coreesponding elements..
For Example: (1)=i/p:
Enter the nos. of list1 seperated by commas:1,2,3
Enter the nos. of list2 seperated by commas:4,5,6
o/p:[5, 7, 9]
(2)=i/p:
Enter the nos. of list1 seperated by commas:2,3,4,5
Enter the nos. of list2 seperated by commas:3,4
o/p:[5, 7, 4, 5]
'''
def main():
    '''
    Purpose:takes inputs for list as a string seperated
    by commas or makes their length equal by appending 0
    further calls function sumList to add the elements
    of the list.
    
    variables:list1,list2,list3
    '''
    list1=[int(x) for x in input("Enter the nos. of list1 seperated by commas:").split(",")]#list comprehension that takes elements of the string separated by commas
    list2=[int(x) for x in input("Enter the nos. of list2 seperated by commas:").split(",")]#list comprehension that takes elements of the string separated by commas
    while len(list1)<len(list2): #checks is list1 length is less than list 2 
        list1.append(0) #appending the list by 0
    while len(list2)<len(list1):#checks is list2 length is less than list 1
        list2.append(0)#appending the list by 0
    list3=sumList(list1,list2)#stors return value of function sumList
    print(list3)#prints the desired list
def sumTwoNum(x,y):
    ''' Purpose:to add two nos.
        Parameters:x,y;the elements of the two lists
        returns the sum
    '''
    z=x+y #adds two nos.
    return z #returns sum of two nos.
def sumList(list1,list2):
    '''
    #code to sum respective elements of these list
    #return list
    parameters:list1,list2
    returns list3 that is sum of nos. of list1 and list2
    '''
    list3=[] #empty list to update sum 
    for i in range(len(list1)):
        x,y=list1[i],list2[i] #takes the element of the lists in x,y
        z=sumTwoNum(x,y) #calls the function sumTwoNum and returns the sum in z
        list3.append(z) #appending the list by sum
    return list3 #returns the list
if __name__=="__main__":
    main() #calling main function
    