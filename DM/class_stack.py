'''
Create a class Stack, to hold records of Student class, having following methods:
1. To push an element on the top of the stack
2. Pop element and display the popped element
3. Peek the top element of the stack 
4. Total elements in the stack

Note: 
1. Push is possible only when stack is not full
2. Pop operation can be performed when stack is not empty 
'''
#Assumptions:
#1.Menu driven program
#2.Stack class with any size; here(user input).
#3.Stack pushes, pops the item given by user.
#4.it shows no. of items in stack and peek element of the stack


class Stack:
    '''
    constructor:size(parameter)
    function:-> isempty:to check stack is empty
                isfull: to check stack is full
                push: to append the record
                pop: to delete the record
                peek: to display the top record
                numOfElements: to display number of records
    '''
    def __init__(self,size):
        self.stackList = []
        self.top = -1 #top element
        self.size = size-1 
    def isempty(self):
        if self.top == -1: #if empty
            return True
        else: #if not empty
            return False
    def isfull(self):
        if self.top == self.size: #if full
            return True
        else:
            return False #if not full
    def push(self,record):
        if self.isfull():
            return f"Stack is full.Can't add more records." #if full
        else:
            self.top=self.top+1 #adding one position to top
            self.stackList.append(record) #appending the list
            return f"Element successfuly pushed."
    def pop(self):
        if self.isempty(): 
            return "Stack is already empty.No record to pop." #if empty
        else:
            pelt = self.stackList.pop() #popping the top element
            self.top=self.top-1 #decreasing top by 1
            return pelt #return popped elt
    def peek(self):
        if self.isempty(): 
            return f"Stack is empty.No peek element." #if empty
        else:
            return self.stackList[self.top] #if not returns the peek element
    def numOfElements(self):
        return self.top+1 #returns the no. of element
if __name__=="__main__":

    size=int(input(f"Enter the size of the stack:"))
    mystack = Stack(size) #creating instance of class Stack
    ch="y"
    while(ch!="n"):
        print("Enter 1 if you want to push the record:")
        print("Enter 2 if you want to see the elements in the stack:")
        print("Enter 3 if you want to pop the record:")
        print("Enter 4 if you want to see the peek record:")
        c=input("Enter your choice:")
        if c=='1':
            print(mystack.push(input("Enter element to push:")))#calling push
            print("stack status")
            for j in mystack.stackList:
                print(j)
        elif c=='2':
            print("No. of elements in stack:",mystack.numOfElements()) 
        elif c=='3':
            print("-----Popped element-----\n",mystack.pop())
        elif c=='4':
            print("-----Peek element-----\n",mystack.peek())
        else:
            print("Wrong choice:")
        ch=input("Enter y to continue and n to exit:")
        