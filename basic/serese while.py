#sum 0f 1+1/2^1+......+1/2^n
import math
sum=0
i=0
n=int(input("enter a number"))
while(i<=n):
    sum=sum+(1/pow(2,i))
    i=i+1
print("sum is ::",sum)