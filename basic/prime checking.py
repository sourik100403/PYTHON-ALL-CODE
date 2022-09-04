#n=int(input("enter the number"))
p=int(input("enter the first number"))
m=int(input("enter the second number"))
for n in range(p,m+1):
 f=0
 for i in range(2,n//2+1):
    if(n%i==0):
        f=1
        break
 if(f==0):
    print(n,"prime number")
 else:
    print(n,"it is not prime number")