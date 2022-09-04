# x=lambda a:a+23
# print(x(2))
# y=lambda a,b:a+b
# print(y(2,3))
# z=lambda a,b,c:a+b-c
# print(z(3,7,5))
# def myfunc(a):
#     return a[1]
# a=[[1,14],[5,6],[8,23]]
# a.sort(key=myfunc)
# print(a)
a=[[1,14],[5,6],[8,23]]
a.sort(key=lambda x:x[1])
print(a)
