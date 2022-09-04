def myfunc(n):
    return lambda a:a*n
mydubler=myfunc(2)
mytribler=myfunc(3)
print(mydubler(11))
print(mytribler(12))