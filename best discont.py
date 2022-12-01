amt=int(input("Enter amount:"))
d1=0.0
d2=0.0
d3=0.0
d1=0.3*amt
d2=0.2*amt
d3=0.1*amt
p1=amt-d1
p2=amt-(d2+d3)
if p1>p2:
    print("First discount best=",p1)
else:
    print("Second discont is best=",p2)