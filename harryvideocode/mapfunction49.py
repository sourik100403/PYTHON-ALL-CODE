def mul(x,y):
    return x*y
def add(x):
    return x+2
list1=[1,2,3,4,5,6,7]
list2=[1,2,3,4,5,6,7]
#list2=list(map((lambda a:a*2),list1))
print("original list1=",list1)
list3=list(map(mul,list1,list2))
print(list3)
