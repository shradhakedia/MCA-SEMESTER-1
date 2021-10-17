def sqsum(n):
    if n==0:
        return 0
    else:
        return n**2 + sqsum(n-1)
n=int(input("Enter the no. upto which you want sum of squares:"))
print("the sum is",sqsum(n))