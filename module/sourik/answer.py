def func(n):
    return lambda a:a*n
doubler=func(2)
tripler=func(3)
print(doubler(11))
print(tripler(11))