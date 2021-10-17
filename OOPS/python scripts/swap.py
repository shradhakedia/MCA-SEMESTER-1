def swap(x,y):
    return y,x
def main():
    x=int(input("first num:"))
    y=int(input("second num:"))
    x,y=swap(x,y)
    print("value of x and y after swapping is:",x,"and",y)
    
   
main()
x="5"
y="10"
print(eval(x+"+"+y))