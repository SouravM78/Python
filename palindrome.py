n=int(input("enter the number: "))
stop=0
def palindrome(x):
    x=str(x)
    a=''
for i in range(-1,-len(x)-1,-1):
    a=a+x[i]
i f a==x:
    return(1)
else:
     return(0)
a=2
number=0
while n>0:
    for j in range(2,a):
        if a%j==0:
            stop=1
            if stop==0:
                if palindrome(a)==1:
                    n=n-1
                    number=a
                    a=a+1
                    print(number)