n=int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j),end='')
    print()
       
b=int(input("enter the another number : "))
for i in range(b):
    for j in range(b):
        print((i,j),end=' ')
    print()
    
c=int(input("enter the another number : "))
for i in range(c):
    for j in range(c):
        print((i,j),end=' ')
    print()
    
d=int(input("enter the another number : "))
for i in range(d):
    for j in range(d):
        print(n-j,end=' ')
    print()
    
e=int(input("enter the another number : "))
for i in range(e):
    for j in range(e):
        print(n-i,end=' ')
    print()
    
f=int(input())
for i in range(f):
    for j in range(f):
        print(max(max(i,j),max(n-j-1,n-i-1)),end=' ')    
    print()
 
g=int(input())
for i in range(g):
    for j in range(g):
        print(
            max(max(i+1,j+1),max(n-j,n-i)
                ),end=" ")
    print()   
    
    
    
    
print(sum([1,2,3,4,5,6,7,8,9]))