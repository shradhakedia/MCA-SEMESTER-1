'''This program counts the no. of words in any string
 and prints it.
 For Example:i/p=Enter the string to count its words : my name is shradha
             o/p=No. of words in string :  4
'''
def main(): #main function to take the input of the input of the user and call countword function

    mystr1=input("Enter the string to count its words : ")
    cntword(mystr1) #calling this function
    
def cntword(mystr1):  #function to count the numbers of words in a string

    count=1 #flag variable count set to 1,so that last word is also counted
    
    l=len(mystr1)
    for i in range(0,l): #for loop to extract words
    
        if mystr1[i]==" ":
            count=count+1 #counting the words as extracted by space character
            
    print("No. of words in string : ",count)

if __name__ == "__main__":
    main() #calling main function
    
    