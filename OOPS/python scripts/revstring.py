''' the program prints the reverse of any string entered by the user
example: i/p= My name is Shradha
         o/p= ahdarhs si eman yM '''

def main(): #main function to get the user input string

    mystr=input("Enter a string to be reversed : ")
    revstring(mystr) #calling the function revstring that prints the reversed string but returns nothing
    
def revstring(mystr):  #function to reverse a string

    print("Reversed string : ",mystr[::-1]) #prints the entire string but from index -1 i.e in reveresed order
    
if __name__ == "__main__":
    main()   #calling main function
