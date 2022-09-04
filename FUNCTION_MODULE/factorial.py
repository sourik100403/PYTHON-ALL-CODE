def factorial(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f
n=int(input("enter any number"))
p=factorial(n)
print("factorial is a",p)

