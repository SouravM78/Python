num=int(input("Enter two digit number:"))
if num>9 and num<100:
    a=num/10
    b=num%10
    s=a+b
    p=a*b
if s+p==num:
    print("Specisl two digit number")
else:
    print("Not a special two digit number")