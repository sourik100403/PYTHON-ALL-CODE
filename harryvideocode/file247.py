def func(x):
    return x+2
list1=[1,2,3,4,5]
list2=list(map(func(list1)))
print(list2)