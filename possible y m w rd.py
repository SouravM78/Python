num=int(input("Enter any number:"))
yr=num/365
temp=num%365
mn=temp/30
a=temp%30
wk=a/7
day=a%7
print("year",yr)
print("month",mn)
print("week",wk)
print("Days",day)