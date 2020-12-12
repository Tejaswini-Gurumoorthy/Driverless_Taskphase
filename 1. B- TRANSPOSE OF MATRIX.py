a=int(input('Enter the number of rows of the matrix: '))
b=int(input('Enter the number of columns of the matrix: '))
m=[[int(input('Enter the elements of the matrix sequentially: '))for i in range(b)]for j in range(a)]
print('The matrix is: ')
for i in range(a):
    for j in range(b):
        print(format(m[i][j]),"   ",end="")
    print()
result=[[0 for i in range(a)]for j in range(b)]
print('The transpose of the matrix is: ')
for i in range(b):
    for j in range(a):
        result[i][j]=m[j][i]
for i in range(b):
    for j in range(a):
        print(format(result[i][j]),"   ",end="")
    print()
    
