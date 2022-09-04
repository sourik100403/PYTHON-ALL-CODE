def add(x,y):
    return x+y
list1=[10,20,30,40,50]
list2=[1,2,3,4,5]
print("original list",list1)
print("original list",list2)
list3=list(map(add,list1,list2))
print("modified list",list3)