n=int(input("enter the number"))
fact=1
if(n==0):
    fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial is ",fact)