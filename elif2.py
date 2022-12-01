a=int(input("First side: "))
b=int(input("Second side: "))
c=int(input("Third side: "))
if a==b and b==c and c==a:
    print("Equilateral Traingle")
elif a==b and b==c or c==a:
    print("isoceles traingle")
else:
    print("scalene Traingle")