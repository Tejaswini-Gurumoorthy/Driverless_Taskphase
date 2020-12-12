#a) Checking if list is a palindrome
li=eval(input('Enter the character list : '))
def check_pal(x):
    if len(x)<=1:
        return "It is a palindrome"
    elif x[0]==x[len(x)-1]:
        return "It is a palindrome"
    else:
        return "It is not a palindrome" 
print(check_pal(li))

#b) Printing hex values
if check_pal(li)=="It is a palindrome":
    print("hex values: ")
    for j in li:
        he=str(hex(ord(j)))
        he=he[2::]
        print(he,end=" ")
#c) Printing diamond pattern
else:
    a=0
    n=len(li)
    for i in range(0,n):
        for j in range(i,n):
            print(" ",end="")
        for k in range(0,2*i+1):
            if k<i:
                print(li[a],end="")
                a+=1
            elif k==i:
                print(li[a],end="")
            else:
                a-=1
                print(li[a],end="")
        print()
    b=0
    for i in range(n-1,0,-1):
        for j in range(i,n+1):
            print(" ",end="")
        for k in range(1,2*i):
            if k<i:
                print(li[b],end="")
                b+=1
            elif k==i:
                print(li[b],end="")
            else:
                b-=1
                print(li[b],end="")
        print()



