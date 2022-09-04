# n=int(input("enter the number"))
# fact=1
# for i in range(n):
#     fact=fact*(i+1)
# print(fact)
# n=int(input("enter the number::"))
# def fact(n):
#     if(n==0):
#         return 1
#     elif(n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# print("factorial of",n,"=",fact(n))
n=int(input("enter the number:"))
def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print("fibbonacci of",n,"=",fibonacci(n))