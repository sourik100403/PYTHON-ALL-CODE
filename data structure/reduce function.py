import functools
def add(x,y):
    return x+y
list1=[10,22,33,55,77]
print("original list",list1)
list2=("sum of element",functools.reduce(add,list1))
print(list2)