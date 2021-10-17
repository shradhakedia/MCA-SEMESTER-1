from class_stack import Stack #importing the stack class

def infixpostfix(exp): 
    #defining the function to convert infix to postfix
    #arguments:exp
    #return:postfix expression string 
    postfixexp="" #taking null strting
    opPrecedence={'^':3,'/':2,'*':2,'+':1,'-':1} #dictionary to set precedence
    for i in exp: #for loop
        if i.isalnum(): #if operand
            postfixexp+=i #adding to the expression
        else:
            if obj.isempty(): #if stack is empty
                obj.push(i) #pushing the operator
            elif opPrecedence[obj.peek()] > opPrecedence[i]: #checking the precendence
                pelt=obj.pop() #if higher precendence operator in stack then pop
                postfixexp+=pelt #add it to the expression
                obj.push(i) #pushing the lower precedence operator in the stack
            else: #if encoutered operator is of higher precedence then the peek element 
                obj.push(i) #pushed the operator
    while not obj.isempty(): #popping the operators i.e. elements of stack
        pelt = obj.pop() #popping the element
        postfixexp+=pelt #adding it to the expression
    return postfixexp #returning the final expression
if __name__ =="__main__": #calling main function
    exp=input("Enter the infix expression to convert to postfix:") #taking the input of the expression
    obj=Stack(len(exp)) #creating the object of class stack
    print(infixpostfix(exp)) #invoking the function and printing the expression returned

            