rev=0
n=int(input("enter a number :"))
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
print("reverse is :",rev)