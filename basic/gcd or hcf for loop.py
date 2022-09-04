n=int(input("enter the biggest number :"))
m=int(input("enter the smaller number :"))
for i in range(1,m+1):
    if(n%i==0 and m%i==0):
        gcd=i
print("gcd is :",gcd)