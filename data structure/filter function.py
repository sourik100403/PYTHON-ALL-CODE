def div_by_three(x):
    if(x%3==0):
        return 1
list1=list(filter(div_by_three,range(2,21)))
print(list1)