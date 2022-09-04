def multi_by_two(x):
    x=x/11
    return x
list1=[11,22,33,44,55,66]
print("original list",list1)
list2=list(map(multi_by_two,list1))
print("modified list is ",list2)