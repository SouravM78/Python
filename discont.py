amt=int(input("Enter amount:"))
dis=0.0
np=0.0
if amt>30000:
    dis=0.20*amt
elif amt>20000 and amt<=30000:
    dis=0.15*amt
elif amt>10000 and amt<=20000:
    dis=0.1*amt
else:
    dis=0.05*amt
np=amt-dis
print("payable amont=",np)