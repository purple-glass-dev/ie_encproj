#Find the transpose of a given matrix.
#Calculate the sum of the elements in each column of the original matrix
cc=1
j=0
import numpy as np
r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of columns :"))
matrix = np.zeros((r,c))
for i in matrix:
    for j in range(c):
        print("Enter element a_",cc,j+1)
        a=int(input())
        i[j] =a
    cc+=1
print(matrix)
print("----------------------------------")
#Finding the transpose of the matrix 
print("Transpose of a matrix")
matrix_t = np.zeros((c,r))
for i in range(r):
   # iterate through columns
   for j in range(c):
       matrix_t[j][i] = matrix[i][j]
print(matrix_t)
print("----------------------------------")
#Finding the sum of elements in each column 
for i in range(c):
        c_sum = 0
        for j in range(r):
            c_sum += matrix[j][i]
        print("Sum of column",i+1,":",c_sum)







