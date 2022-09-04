import functools
# def add(x,y):
#     return x+y
list1=[10,20,30,40,50]
list2=("sum of",functools.reduce(lambda x,y:x-y,list1))
print(list2)