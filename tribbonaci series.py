a=0
b=1
c=1
print(a," ",b," ",c)
for i in range(1,9):
    d=a+b+c
    print(" ",d)
    a=b
    b=c
    c=d