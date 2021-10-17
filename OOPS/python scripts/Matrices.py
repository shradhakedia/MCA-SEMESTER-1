'''The following script takes a matrix
   finds the trace and A.*A (Hadamard product)
   and A*A( multiplication)
'''
import numpy as np
import sympy

def main():
    '''Purpose:Takes one matrix and find its trace,HamDard Product
                with itself and its multiplication with itself.
       Variables:n,a,matrix,prodmatrix,mul_matrix
    '''
    n=int(input("Enter the no. of rows for square matrix:"))    
    matrix=[]
    #creating the matrix
    for i in range(n):
        a=[]
        for j in range(n):
            a.append(int(input(f"Enter the row {i+1} column {j+1} element:")))
        matrix.append(a)
    #printing the matrix
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end="\t")
        print()
    #printing the trace
    print("The sum of diagonal elements of the matrix is:",trace(matrix,n))
    #taking the returned matrix of hamdard_product in prodmatrix
    prodmatrix=hadamard_product(matrix,n)
    print("The Hadamard product of the matrix:")
    #printing the Hadamard product
    for i in range(n):
        for j in range(n):
            print(prodmatrix[i][j],end="\t")
        print()
    #recieving the returned multiple matrix from multiply_matrix
    mul_matrix=multiply_matrix(matrix,n)
    print("The multiplication of two matrices is:")
    #printing the multiplication of two matrices
    for i in range(n):
        for j in range(n):
            print(mul_matrix[i][j],end="\t")
        print()
    #finding determinant
    print("The determinant of the matrix is:",end="")
    print(np.linalg.det(matrix))
    #linearly independent vectors
    red_matrix, inds = sympy.Matrix(matrix).T.rref()
    print("Independent vectors")
    for i in inds:
        print(matrix[i])
        
def trace(matrix,n):
    '''Purpose:to find the sum of diagonal elements
       Parameters:matrix,n
       returns trace
    '''
    tr=0
    for i in range(n):
        for j in range(n):
            if i==j:
                tr=tr+matrix[i][j]
    return tr
    
def hadamard_product(matrix,n):
    '''Purpose:finds product and returns it
       Parameters:matrix,n
       returns the prodmatrix
    '''
    prodmatrix=[]
    for i in range(n):
        a=[]
        for j in range(n):
            elt=matrix[i][j]**2
            a.append(elt)
        prodmatrix.append(a)
    return prodmatrix
    
def multiply_matrix(matrix,n):
    '''Purpose:finds multiplication and returns it
       Parameters:matrix,n
       returns the mul_matrix
    '''
    mul_matrix=[]
    sums=0
    for i in range(n):
        a=[]
        for j in range(n):
            for k in range(n):
                elt=matrix[i][k]*matrix[k][j]
                sums=sums+elt
            a.append(sums)
            sums=0
        mul_matrix.append(a)
    return mul_matrix
if __name__=="__main__":
    main()