'''Given any number, The program returns the corresponding text in words but in reverse order.
If it is a character, then take its ASCII value and reversed it.
Also, inserted a space between each encoded o/p.
For any special character, take it as it is

e.g. if input is : 3AD$2a
o/p:  eerht 56  86 $ owt 79

For decoding, the reverse of above is conducted.
i.e. input: eerht 56  86 $ owt 79
output: 3AD$2a
'''
def main(): #the main function
    print("--Message from Goofy--")
    message=input("Enter the message to Encode:") #taking input from the user
    encoded=encode(message) #calling the encode function and storing the return value in  encoded
    print("The encoded message is:",encoded) #print the encoded message
    decoded=decode(encoded) #calling the decode function and storing the return value in  decoded
    print("The decoded message is:",decoded) #print the decoded message
def encode(message): 
    '''
    Purpose:to take the input and encode it accordingly as specified above
    parameters:message
    returns:encoded message
    '''
    arr={"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"} #dictionary to store corresponding nos.
    encoded="" #null string to store encoded message
    for i in message: #for loop to trascate each character
        if i.isnumeric(): #checking if character is a digit
            s=arr[i] #taking corresponding string to that no.
            encoded+=s[::-1]+" " #storing the encoded message
        elif i.isalpha(): #checking if character is a alphabet
            s=str(ord(i)) #returning ascii value in string form
            encoded+=s[::-1]+" " #storing the encoded message
        elif i.isspace():
            encoded+="23"+" "
        else:
            encoded+=i+" "  #storing the encoded message
    return encoded    #returning the encoded message
def decode(encoded):
    '''
    Purpose:to take the encoded message and decode it accordingly as specified above
    parameters:encoded
    returns:decode message
    '''
    message=encoded.strip().split(" ") #storing the encoded message word by word separated by space
    arr={"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"} #dictionary to store corresponding nos.
    decoded="" #null string to store encoded message
    for word in message:#for loop to trascate each word
        s=word[::-1] #reversing the word
        if s in arr: #checking membership of s in arr dictionary
            decoded+=arr[s]  #storing the decode message
        elif s.isnumeric(): #checking if s is a numeric
            decoded+=chr(int(s)) #converting a string into a integer then that ascii integer in char
        else:
            decoded+=s #storing the decode message
    return decoded #returning the decode message


if __name__ == "__main__":
    main() #main function