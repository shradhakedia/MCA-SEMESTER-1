from class_stack import Stack #importing the stack class

def Paranthesischecker(exp): 
    #defining the function to check paranthesis
    #arguments:exp
    #return:bool type
    for i in exp: #for loop
        if i in "{([": #checking opening brackets in expression
            obj.push(i) #pushing the element
        else: 
            #if closing brackets in expression
            #stack must not be empty 
            #i.e. to pop the  elt we need opening brackets in the stack
            if obj.isempty(): #if empty
                return False 
            pelt=obj.pop() #popping element
            if pelt=='(': #matching if the popped element is '(' opening brackets
                if i!=')': #the current character is not ')'
                        return False
                elif pelt=='{':  #matching if the popped element is '{' opening brackets
                    if i!='}': #the current character is not '}'
                        return False
                elif pelt=='[':  #matching if the popped element is '[' opening brackets
                    if i!=']':
                        return False #the current character is not ']'
            else:
                return True #else return true
    
if __name__=="__main__": #calling main function
    exp=input("Enter the expression with parenthesis:") #taking input from the user
    obj = Stack(len(exp)) #making object of class Stack
    if Paranthesischecker(exp): #if returns true
        print("Balanced")
    else: #if returns false
        print("Unbalanced")











