#sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........
import math
x=int(input("enter the value of x :"))
n=int(input("enter the value of n :"))
sum=0.0
pos=1
for i in range(1,n+1,2):
    f=1
    for j in range(1,i+1):
        f=f*j
        print(f)
        if(pos%2==0):
            sum=sum-pow(x,i)/f
        else:
            sum = sum+pow(x, i) / f
        pos=pos+1
print("sum is :",round(sum,2))