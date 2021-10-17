'''
Write a Python function encrypt that takes a sentence as input from the user and  returns the encrypted message
using the following rules: 
uppercase alphabet is replaced with shift formula (i+6)%26, where i is ASCII  value of the alphabet, lowercase alphabet 
is replaced by (i-3)%26, where i is  ASCII value of the alphabet, a digit (0 to 9) is replaced by a character whose ASCII  
value is computed as (square(digit)+5)%26+65, and a special character is kept as it is. A space is added after each encoded
letter/digit.  Also, design a function decrypt to decrypt the message. 
'''


def encrypt(message):
    encoded="" #null string to store encoded message
    for i in message: #for loop to trascate each character
        if i.isnumeric(): #checking if character is a digit
            s=((int(i)**2)+5)%26 +65
            s=chr(s)
            encoded+= s + " " #storing the encoded message
        elif i.isupper(): #checking if character is a alphabet
            s=(ord(i)+6)%26 #returning ascii value in string form
            s=str(s)
            encoded+=s+" " #storing the encoded message
        elif i.islower(): #checking if character is a alphabet
            s=(ord(i)-3)%26 #returning ascii value in string form
            s=str(s)
            encoded+=s+" " #storing the encoded message
        else:
            encoded+=i+" "  #storing the encoded message
    return encoded    #returning the encoded message
encoded=encrypt("ab   c3 Aa")
print(encoded)
def decrypt(encoded):
    '''A->19 (65+6)%26=19
       d->19 (100-3)%26=19
       (in the case error occurs as 19 can be decrypted either to A or d )
       it works fine for lowercase letters for upper case like A it will give output d and so on for B-Z
    '''
    count=0
    message=encoded.strip().split(" ")
    print(message)
    alphabet={"F":0,"G":1,"J":2,"O":3,"V":4,"E":5,"P":6,"C":7,"R":8,"I":9}
    decoded="" #null string to store encoded message
    for i in message: #for loop to trascate each character
        if i.isnumeric(): #checking if character is a digit
            if int(i)>=16:
                s=chr(97+(int(i)-16))
            elif int(i)<16:
                s=chr(107+int(i))
            decoded+= s #storing the encoded message
        elif i.isalpha(): #checking if character is a alphabet
            s=alphabet[i]
            decoded+=str(s) #storing the encoded message
        elif i=='':
            count+=1
            if count==2: 
                decoded+=" "
                count=0
        else:
            decoded+=i  #storing the encoded message
    return decoded    #returning the encoded message
print(decrypt(encoded))
