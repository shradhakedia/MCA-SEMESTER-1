'''Implement Queue class, having following functions:
1. Enqueue: to insert an element, before insertion check queue is not full. 
2. Dequeue: to delete an element, before deletion, check queue should not be empty.
3. Display: to display elements of the list

Note: 
1. Enqueue is possible only when queue is not full
2. Dequeue can be performed when queue is not empty 
3. The size of queue is fix i.e. queue can have a limited number of elements.
'''
#Assumptions:
#1.Circular queue class with any size; here(capacity).
#2.queue enqueues the item at rear, dequeues the items at front.
#3.enqueue,dequeue,frontelt,rearelt,display queue are applied randomly in main function.
class Queue:
    '''
    constructor:self,capacity(arguments)
    function:-> isempty:to check queue is empty
                isfull: to check queue is full
                enqueue: to add the item
                dequeue: to delete the item at front
                frontelt: to display the front element
                rearelt: to display the rear element
                str:to display the queue
    '''
    def __init__(self,capacity): 
        '''
        capacity:to hold the maximum elements that queue can store
        front:for front elt (to dequeue)
        rear: for rear elt (to enqueue)
        size: for current size of queue
        queue: queue list of size as capacity given by the user
        '''
        self.capacity=capacity
        self.front=0
        self.rear=capacity-1
        self.size=0
        self.queue=['']*self.capacity
    def isfull(self):
        if self.size==self.capacity: #if full
            return True
        else: #if not full
            return False
    def isempty(self):
        if self.size==0: #if empty
            return True
        else: #if not empty
            return False
    def enqueue(self,item):
        if self.isfull():
            return f"Queue full,can't add more item." #when full
        else:
            self.rear=(self.rear+1) % self.capacity #updating rear
            self.queue[self.rear]=item #inserts element at rear
            self.size+=1
            return f"Element enqueued,{item}"
    def dequeue(self):
        if self.isempty():
            return f"Queue empty,can't remove more items."
        else:
            pelt=self.queue[self.front] #front elt
            self.queue[self.front]='' #setting front to ''
            self.front=(self.front+1)%self.capacity #updating front
            self.size-=1
            return f"Element dequeued,{pelt}"
    def frontelt(self):
        if self.isempty():
            return f"Queue empty,no element at front" #when empty
        else:
            return f"Element at front,[{self.queue[self.front]}]" #returns element at front
    def rearelt(self):
        if self.isempty():
            return f"Queue empty,no element at rear" #when empty
        else:
            return f"Element at rear,[{self.queue[self.rear]}]" #returns element at rear
    def __str__(self):
        if self.size==0:
            return "Queue is empty"
        elif self.rear<self.front:
            return f"Queue is:{self.queue[self.front:self.capacity]+self.queue[0:self.rear+1]}"
        else:
            return f"Queue is:{self.queue[self.front:self.capacity]} " #returns queue list
if __name__=="__main__": #calling main function
    capacity=int(input(f"Enter the capacity of the Queue:"))
    myqueue = Queue(capacity) #creating instance of class Stack
    ch="y"
    while(ch!="n"):
        print("Enter 1 if you want to enqueue the element:")
        print("Enter 2 if you want to dequeue the element:")
        print("Enter 3 if you want to see the element at front:")
        print("Enter 4 if you want to see the element at rear:")
        print("Enter 5 if you want to see the queue:")
        c=input("Enter your choice:")
        if c=='1':
            print(myqueue.enqueue(input("Enter element to push:")))
        elif c=='2':
            print(myqueue.dequeue()) 
        elif c=='3':
            print(myqueue.frontelt())
        elif c=='4':
            print(myqueue.rearelt())
        elif c=='5':
            print(myqueue)
        else:
            print("Wrong choice:")
        ch=input("Enter y to continue and n to exit:")