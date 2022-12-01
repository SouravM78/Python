n=int(input("Enter Limit:"))
se=0
so=0
for i in range(1,n+10):
    if i%2==0:
        se=se+i
    else:
        so=so+i
print("Even sum",se)
print("odd sum",so)