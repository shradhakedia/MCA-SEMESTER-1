from class_stack import Stack  #importing Stack class 
if __name__=="__main__": #calling main function
    exp =list(map(str,input("Enter the numeric postfix expression separated by space:").split())) #taking the input from the user
    stackObj = Stack(len(exp)) #creating object of stack class
    for i in exp: #for loop
        if i.isnumeric(): #checking if character is numeric
            stackObj.push(i) #pushing it into stack
        else: #if encountering with an operator
            oprnd2 = stackObj.pop() #poping the operand
            oprnd1 = stackObj.pop() #poping the operand
            stackObj.push(str(eval(oprnd1+i+oprnd2))) #pushing the evaluated expression
    print("The evaluated postfix expression is:",stackObj.peek()) #printing the peek element(The evaluated expression)