a=int(input("Enter the number of rows of matrix A : "))
b=int(input("Enter the number of columns of matrix A :"))
d=int(input("Enter the number of rows of matrix B : "))
c=int(input("Enter the number of columns of matrix B : "))
if(b==d):
   A=[[int(input('Enter the elements of matrix A sequentially :  '))for i in range(b)]for j in range(a)]
   print('matrix 1: ')
   for i in range(a):
       for j in range(b):
           print(format(A[i][j]),"   ",end="")
       print()
   B=[[int(input('Enter the elements of matrix B sequentially :  '))for i in range(c)]for j in range(d)]
   print('matrix 2: ')
   for i in range(d):
       for j in range(c):
          print(format(B[i][j]),"   ",end="")
       print()
   AB=[[0 for i in range(c)]for j in range(a)]
   for i in range(a):
       for j in range(c):
           for k in range(d):
               AB[i][j]+=A[i][k]*B[k][j]
   print('The product of matrices A and B is: ')
   for i in range(a):
       for j in range(c):
           print(format(AB[i][j]),"   ",end="")
       print()
   AB_trans=[[0 for i in range(a)]for j in range(b)]
   print("The transpose of the product of matrices A and B is  : ")
   for i in range(b):
       for j in range(a):
           AB_trans[i][j]=AB[j][i]
   for i in range(b):
       for j in range(a):
           print(format(AB_trans[i][j]),"   ",end="")
       print()
   B_trans=[[0 for i in range(d)]for j in range(c)]
   print('The transpose of matrix B is : ')
   for i in range(c):
       for j in range(d):
           B_trans[i][j]=B[j][i]
   for i in range(c):
       for j in range(d):
           print(format(B_trans[i][j]),"   ",end="")
       print()
   A_trans=[[0 for i in range(a)]for j in range(b)]
   print('The transpose of matrix A is : ')
   for i in range(b):
       for j in range(a):
           A_trans[i][j]=A[j][i]
   for i in range(b):
       for j in range(a):
           print(format(A_trans[i][j]),"   ",end="")
       print()
   B_A=[[0 for i in range(a)]for j in range(c)]
   for i in range(c):
       for j in range(a):
           for k in range(b):
               B_A[i][j]+=B_trans[i][k]*A_trans[k][j]
   print("The product of B transpose and A transpose is : ")
   for i in range(c):
       for j in range(a):
           print(format(B_A[i][j]),"   ",end="")
       print()
   print("HENCE PROVED THAT (AB)'=B'A' !! ")
else:
    print('ERROR!!!! Please make sure that the number of columns of the first matrix is equal to the number of rows of the second matrix')
                
