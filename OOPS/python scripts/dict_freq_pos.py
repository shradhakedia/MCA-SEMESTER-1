'''This program takes a user input list
finds the frequency and position 
of all the elements in the list
For Example: input=
Enter the no. of elements in the list:8
Enter 1 element:
1
Enter 2 element:
2
Enter 3 element:
3
Enter 4 element:
2
Enter 5 element:
3
Enter 6 element:
1
Enter 7 element:
1
Enter 8 element:
1

Output=
list: [1, 2, 3, 2, 3, 1, 1, 1]
for frequency:
Items                   Frequency
1                        4
2                        2
3                        2
for position:
Items                   Position
1                       1,6,7,8,
2                       2,4,
3                       3,5,
'''
def main():
    """The main function takes the entry from the user
    for the list and then calls the function freq_pos 
    to get the frequency and position of the numbers of
    list.
    """
    n=int(input("Enter the no. of elements in the list:")) #no. of elements of the list
    userslist=[] #emptylist to store user inputs
    for i in range(0,n): #for loop to take inputs
        userslist.append(int(input(f"Enter {i+1} element"))) #appending the list with the elements
    print("list:",userslist,"\nfor frequency:\nItems\t\t\tFrequency") #printing the list
    frequency,position=freq_pos(userslist) #catches the returned value of the function freq_pos
    for x,y in frequency.items():#loop to print the desired pattern for elements and frequency
        print(x,"\t\t\t",y)
    print("for position:\nItems\t\t\tPosition")
    for x,y in position.items():#loop to print the desired pattern for items and position
        print(x,end="\t\t\t")
        for i in range(len(y)):#loop accesing the element of position list
            print(y[i],end=",")
        print() #takes the control to next line
def freq_pos(userslist):
    """This function takes the user list and
    returns the frequency and position
    the elements of that list"""
    position={} #empty dictionary to store positions
    frequency={i:userslist.count(i) for i in userslist} #dictionary comprehension for counting the frequency
    for i in range(len(userslist)):#loop to store the positions in the position dictionary
        if userslist[i] not in position: #checks if the element is not present in list
            position[userslist[i]]=[i+1]#creates a list with position of the element
        else:#else element is already present in list
            position[userslist[i]].append(i+1)#appends the list with the position 
    return frequency,position #returns the dictionary that has frequency and position
print(freq_pos.__doc__)
help(freq_pos)
if __name__=="__main__":
    main() #calls main function
