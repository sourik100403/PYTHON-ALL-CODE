def greatest_check(a,b,c):
    if(a>b and a>c):
        print(a,'is a greatest number')
    elif(b>a and b>c):
        print(b,"is greatest number")
    else:
        print(c,"is a greatest number")
a=int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
greatest_check(a,b,c)

