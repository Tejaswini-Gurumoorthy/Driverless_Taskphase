# 2. A) removing duplicate elements
x=eval(input('Enter the tuple '))
li=list(x)
for i in li:
    while li.count(i)>1:
        li.remove(i)
x=tuple(li)
print(x)
# 2. B) sum of tuple using recursion
def add(i):
    if i==1:
        return x[0]
    else:
        return x[i-1]+add(i-1)
print('The sum of tuple elements')
print(add(len(x)))

