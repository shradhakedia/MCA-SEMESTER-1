'''This program counts the vowels,consonants and special characters
in a given string.
For Example: i/p=Enter the string to count vowels, consonants and special characters : shradha&
             o/p=No. of vowels :  2
                 No. of consonants : 5
                 No. of special characters : 1
'''
def main():
    mystr1=input("Enter the string to count vowels, consonants and special characters : ")
    countchar(mystr1) #calling this function for printing no. of vowels,consonants and special characters
    
def countchar(mystr1):    #function to count no. of vowels, consonants and special characters

    vowels,cons,special = 0,0,0     
    mystr=mystr1.lower()   #converting the string to lowercase letters
    
    for i in mystr: #loop to check specified character
    
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u': #if condition to check vowels
        
            vowels+=1
        elif i>='a' and i<='z': #elif to check consonants(vowels would not enter here)
        
            cons+=1
        elif (not(i>='0' and i<='9')): #elif to check other special characters(consonants and vowels will not enter here)
        
            special+=1        
    print("No. of vowels : ",vowels)
    print("No. of consonants :",cons)
    print("No. of special characters :",special)

if __name__ == "__main__":
    main() #calling main function
