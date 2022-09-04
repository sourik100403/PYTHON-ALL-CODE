#import math
n=int(input("eneter the number"))
sum=0.0
for i in range(0,n+1):
    sum=sum+(1/(2**i))
print("sum is ",sum)