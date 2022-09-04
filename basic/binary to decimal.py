#binary to decimal
i=0
sum=0
n=int(input("enter the number :"))
while(n>0):
     r=n%10
     sum=sum+r*pow(2,i)
     i=i+1
     n=n//10
print("decimal is :",sum)