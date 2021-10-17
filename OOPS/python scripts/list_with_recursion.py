'''The following program has several functions that are called recursively to perform the following task:
1)Flatten a list
2)Copy a list
3)Deep copy of a list
o/p:The copy of list is: [2, 5, [5, 6, 8], [1, 2], [5], 3]
    The list after flattening is: [2, 5, 5, 6, 8, 1, 2, 5, 3]
    The deep copy of the list is: [2, 5, [5, 6, 8], [1, 2], [5], 3]
'''
def main(): #the main function
    list1=[2,5,[5,6,8],[1,2],[5],3] #list
    print("The copy of list is:",copylist(list1)) #printing the copy list by calling the copylist() function
    print("The list after flattening is:",flatlist(list1)) #printing the flatten list by calling flatlist() function
    print("The deep copy of the list is:",deepcopy(list1)) #printing the deep copy list by calling deepcopy() function
    print("The cumulative elements of the list is",cumlativefrequency([1,2,3],0))
#copying the list
def copylist(list1): 
    '''Purpose:To copy the list1
       Arguments:list1
       Return:returns the copy of the list
    '''
    if list1==[]: #checks if list is empty
        return [] #returns the empty list
    else:
        return [list1[0]] + copylist(list1[1:]) #returns a list with element at index 0 and calls recursively copylist function from 1st index to the end
#fattening the list
def flatlist(list1):
    '''Purpose:To flat the list1
       Arguments:list1
       Return:returns the flatten list
    '''
    if list1==[]:#checks if list is empty
        return [] #returns the empty list
    elif type(list1[0]) is int: #checks if list at index 0 is integer or further a list 
        return [list1[0]] + flatlist(list1[1:]) #returns a list with element at index 0 and calls recursively copylist function from 1st index to the end
    else: #if its list
        return flatlist(list1[0]) + flatlist(list1[1:]) #returns the calling again the list at index 0 to flat and the original list from index 1 to end
#deepcopying the list
def deepcopy(list1):
    '''Purpose:To deepcopy the list1
       Arguments:list1
       Return:returns the deepcopy list
    '''
    if list1==[]: #checks if list1 is empty
        return [] #returns an empty list
    elif type(list1[0]) is int: #checks if list at index 0 is integer or further a list
        return [list1[0]] + deepcopy(list1[1:])#returns a list with element at index 0 and calls recursively copylist function from 1st index to the end
    else: #if its list
        return [deepcopy(list1[0])] + deepcopy(list1[1:]) #retruns the list by calling again the list at index 0 and the original list from index 1 to end
def cumlativefrequency(_list,sum):
    if not _list:
        return list()
    sum+=_list[0]
    return [sum]+cumlativefrequency(_list[1:],sum)

if __name__=="__main__":
    main() #calling main function
