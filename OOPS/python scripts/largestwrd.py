'''This program takes a input string from a user 
and prints the largest word of that string.

For example: i/p=Enter a string :apple is a fruit
             o/p=The largest word is apple and its length is 5
                 The largest word is fruit and its length is 5'''
def main(): #main function to take input as a string and calling the function largest

    mystr=input("Enter a string :")
    largest(mystr) #calling function largest
    
def largest(mystr): #to print the largest word of a string

    list1=mystr.split(" ") #spliting the string into a list
    
    word=max(list1,key=len) #finding word of maximum length
    
    length1=len(word)
    for i in list1: #to find the words in list that are of maximum length
    
        if len(i)==length1: #checking length of word is same as taht of maximum length
        
            print("The largest word is",i,"and its length is",length1)

if __name__ == "__main__":
    main() #calling main function
