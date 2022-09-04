import math
bin=0
i=0
dec=int(input("enter a number :"))
while(dec>0):
    r=dec%2
    bin=bin+r*pow(10,i)
    dec=dec//2
    i=i+1
print("binary is ::",bin)