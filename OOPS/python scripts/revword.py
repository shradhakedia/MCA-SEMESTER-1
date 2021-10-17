''' This program prints the string with its words reversed 
For Example-i/p=Enter a string whose words are to be reversed : my name is shradha
        o/p=Reversed words of the string :
ym eman si ahdarhs
'''

def main():
    mystr=input("Enter a string whose words are to be reversed : ")
    revword(mystr) #calling the function revword
    
def revword(mystr): #function to print the reverse word 

    word="" #to store the word
    
    l=len(mystr) 
    print("Reversed words of the string : ")
    for i in range(0,l): #for loop to extract the word
    
        if mystr[i]!=" ":
            word=mystr[i]+word #storing the reversed word  
             
        else:
            print(word,end=" ")
            word="" #setting word to null again
            
    print(word) 
    ''' to print the last word that couldn't 
    be extracted by loop die to space missing at the end of the string'''
    
if __name__ == "__main__":
    main()