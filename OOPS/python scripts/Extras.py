'''
list1=[7,6,4,3,9,3,2]
l=list1.copy()
l.remove(max(l))
print(max(l))


#function returning a function...decorater starts here
def create_adder(x):  
    def adder(y):  
        return x+y  
  
    return adder  
  
add_15 = create_adder(15)  
  
print(add_15(10))
'''
'''
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

#square
from turtle import *
for i in range(4):
    forward(200)
    right(90)

#star
import turtle
obj = turtle.Turtle()

for i in range(5):
    obj.forward(100)
    obj.right(144)

import turtle
turtle.color('blue')
style = ('Courier', 90, 'normal')
turtle.write('SHRADHA', font=style, align='center')
turtle.hideturtle()	
turtle.done()
'''

'''
def cumlativefrequency(_list,sum):
    if not _list:
        return list()
    sum+=_list[0]
    return [sum]+cumlativefrequency(_list[1:],sum)
cl=cumlativefrequency([1,2,3],0)
print(cl)
'''
'''
def divk(n,k):
    for i in range(1,n//2+1):
        if n%i==0:
            l.append(i)
    l2=list(filter(lambda x: len(str(x))==k,l))
    if l2!=[]:
        return f"divisor is {max(l2)}"
    else:
        return "no such divisor"
if __name__=="__main__":
    n,k=map(int,input("Enter:").split())
    if k>len(str(n)):
        print("invalid k value")
    else:
        l=[n]
        s=divk(n,k)
        print(s)
'''
'''
#n=2,k=3
#output 998
#m=999
#n=2,k=1
#m=9,m%n==0 then m else m-m%n
def fun(k,n):
    if k>0:
        m=str(9)*k
        m=int(m)
    if k<=0 or n<=0 or m<n:
        raise Exception("Invalid Input")
    while m:
        if m%n==0:
            return m
        else:
            m-=1
m=fun(3,0)
print(m)
'''
'''
#quick sort,merge sort,tower of hanoi
#printing 1,2,3,4,5 by recursion
#stack pr utarte huye kaam karna hai
def sequenceinc(n):
    #base case
    if n==0:
        return
    #recursive assumption
    sequenceinc(n-1)
    #self work
    print(n)
sequenceinc(5)
#priniting 5,4,3,2,1 by recursion
#stack pr chadte huye kaam karna hai
def sequencedec(n):
    #base case
    if n==0:
        return
    #self work
    print(n)
    #recursive assumption
    sequencedec(n-1)
sequencedec(5)
'''
'''
#5,4,3,2,1,2,3,4,5
def func(n):
    #base case
    if n==1:
        print(1)
        return 
    #self work
    print(n)
    #recursive assumption
    func(n-1)
    #self work
    print(n)
func(5)
'''
print(6*1/2)