'''This script finds the outer product amd max and min
   of vectors from scratch without using any predefined libraries.
   it contains main,outer_prod,maximum and minimum as functions
'''
def main():
    '''Purpose:This function takes two vectors input from user
               print their outer product and finds maximum and
               minimum element from them. 
       Parameters:n,m that take no. of elements in row 1 and 2
                  vector1,vector2 that stores the elememts
    '''
    n=int(input("Enter no. of elements for the first vector:"))
    vector1,vector2=[],[]
    for i in range(n):
        vector1.append(int(input(f"Enter element {i+1}:")))
    m=int(input("Enter no. of elements for the second vector:"))
    for i in range(m):
        vector2.append(int(input(f"Enter element {i+1}:")))
    '''recieving the returned outer product 
    from the function outer_prod and printing the same'''
    outerprod=outer_prod(vector1,vector2)
    print("The outer product of the vectors is:")
    for i in range(len(vector1)):
        for j in range(len(vector2)):
            print(outerprod[i][j],end=" ")
        print()
    ''' recieving the max and min elements of vector1 
    and prints it'''
    max1,min1=max_min(vector1)
    print("maximum of vector1 is:",max1,"\nminimum of vector1 is:",min1)

def outer_prod(vector1,vector2):
    ''' Purpose: To find outer product
        Parameters:vector1,vector2
        Returns:A double dimension list that is outer product
    '''
    outerprod=[]
    for i in range(len(vector1)):
        row=[]
        for j in range(len(vector2)):
            prod=vector1[i]*vector2[j]
            row.append(prod)
        outerprod.append(row)
    return outerprod
    
def max_min(vector1):
    '''Purpose:To find maximum and minimum of vector1
       Parameters:vector1
       Returns:integers that is maximum and minimim 
    '''
    max1=0
    min1=vector1[0]
    for i in vector1:
        if max1<i:
            max1=i
    for i in vector1:
        if min1>i:
            min1=i
    return max1,min1

if __name__=="__main__":
    main()