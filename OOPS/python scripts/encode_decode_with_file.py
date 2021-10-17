'''This Program creates three text file,one to store message of Ms. Goofy,second to store the encoded text and third to store decoded text
------------------Encoding and Decoding is done in this format---------------------------------
Given any number, The program returns the corresponding text in words but in reverse order.
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
    with open("Message.txt","w+") as f:#opening a file in w+ mode to create,overwrite and read the message of Goofy
        p=f.write("Your secret message is:\n") #writing the following message
        f.write(input("Enter your secret message:") + "\n") #writing the secret message in file entered by user
        print("Your message is saved in text file name,Message.txt") #print the following message
        f.seek(p) #setting the pointer before the message that is to encoded
        message=f.read() #reading the message
    print("Your encoded message is saved in the file name encoded.txt...\nKindly check!") #printing the following message
    with open("Encoded.txt","w+") as e: #opening a file in w+ mode to create,overwrite and read the encoded message
        p=e.write("the encoded message is:\n")  #writing the following message
        e.write(encode(message)+"\n") #writing the encoded message
        e.seek(p) #setting the pointer before the encoded message
        encoded=e.read() #reading the encoded message
    print("Your decoded message is saved in the file name decoded.txt...\nKindly check!") #printing the following message
    with open("decoded.txt","w+") as d: #opening a file in w+ mode to create and overwrite the decoded message
        d.write("the decoded message is:\n")#writing the following message
        d.write(decode(encoded)) #writing the decoded message
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