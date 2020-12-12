a=int(input("Enter the number of rows of matrix 1 "))
b=int(input("Enter the number of columns of matrix 1 "))
d=int(input("Enter the number of rows of matrix 2 "))
c=int(input("Enter the number of columns of matrix 2 "))
if(b==d):
   m1=[[int(input('Enter the elements of matrix 1:  '))for i in range(b)]for j in range(a)]
   print('matrix 1: ')
   for i in range(a):
       for j in range(b):
           print(format(m1[i][j]),"   ",end="")
       print()
   m2=[[int(input('Enter the elements of matrix 2:  '))for i in range(c)]for j in range(d)]
   print('matrix 2: ')
   for i in range(d):
       for j in range(c):
          print(format(m2[i][j]),"   ",end="")
       print()
   result=[[0 for i in range(c)]for j in range(a)]
   for i in range(a):
       for j in range(c):
           for k in range(d):
               result[i][j]+=m1[i][k]*m2[k][j]
   print('The product of matrix 1 and matrix 2')
   for i in range(a):
       for j in range(c):
           print(format(result[i][j]),"   ",end="")
       print()
else:
    print('ERROR!!!! Please make sure that the number of columns of the first matrix is equal to the number of rows of the second matrix')
                
                
         
