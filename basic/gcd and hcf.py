#gcd check
n=int(input("enter the bigger number :"))
m=int(input("enter the smaller number :"))
while(1):
    r=n%m
    if(r==0):
        hcf=m
        print("hcf is :",hcf)
        break
    else:
        n=m
        m=r
