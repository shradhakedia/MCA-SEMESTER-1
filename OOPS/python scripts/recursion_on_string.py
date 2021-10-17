'''
The following program has several functions that are called recursively to perform the following task:
1)no. of elements in a string
2)reversing the string
3)checking palindrome string or not
'''

def main(): #takes the input string and prints the result of the above mentioned tasks 
    s=input("Enter the string:") #entry from user
    print("The no. of elements in the string is",length(s)) #printing the length of s
    print("The rev string of the string is:",revstr(s)) #printing the reverse of the string
    print("The given string is palindrome or not:",palindrome(s)) #printing true or false if the string is palindrome
#no. of elements in a string
def length(s):
    '''Purpose:To find no. of elements in a string given by the user
       Arguments:s
       Return:returns the length of the string s
    '''
    if s=="": #checks if string is null
        return 0 #returns 0 if condition is true
    else:
        return 1+length(s[1:]) #returns sum of 1 and the rest of the string from index 1 to end
#reversing the string
def revstr(s):
    '''Purpose:To reverse the string given by the user
       Arguments:s
       Return:returns the reverse of the string
    '''
    if s=="": #checks if string is null
        return "" #returns null string when condition is true
    else:
        return revstr(s[1:])+s[0] #returns the function with arguments as string from index 1 to end and string at index 0; or return s[-1]+revstr(s[:-1])
#palindrome string
def palindrome(s):
    '''Purpose:To check if the string given by the user is palindrome or not
       Arguments:s
       Return:returns bool value
    '''
    if s=="": #checks if string is null
        return True #returns true if condition is true
    elif s[0]==s[-1]: #checks if first character is same as last char
        return palindrome(s[1:-1]) #calls the function again as string leaving its first and last char
    else:
        return False #returns false if both condition is false
if __name__=="__main__":
    main() #calling main function