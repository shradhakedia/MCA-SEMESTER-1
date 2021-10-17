'''The Program takes input x from a user and
prints the factorial from 1 to x and x to 1
For Example: i/p:Enter a number:7
             o/p:The factorial from 1 to 7 is [1, 2, 6, 24, 120, 720, 5040]
                 The factorial from 7 to 1 is [5040, 720, 120, 24, 6, 2, 1]
'''
def main():
    '''Purpose:The main function returns takes input from the user
          and calls the function fact() with parameter x,list1
       Variable:x,list1
       Arguments:x,list1
    '''
    x=int(input("Enter a number greater than 0:")) #taking the input from the user
    list1=[] #empty list to store factorials
    fact(x,list1) #calling the function
    print(f"The factorial from 1 to {x} is {list1}")
    print(f"The factorial from {x} to 1 is {list1[::-1]}")
def fact(x,list1): 
    '''Purpose:To append the list with factorials and
    call the itself till the number is greater than 0 and return the factorial everytime
    '''
    if x>0: #checks if number is greater than 0
        result=x*fact(x-1,list1) #multiplies the no. by calling the function itself
        list1.append(result) #appending the list with multiples
    else:
        result=1 #if number is 0,result updates to 1
    return result #returns result
if __name__=="__main__":
    main() #calling main function