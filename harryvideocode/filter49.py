# def greater5(num):
#     return num>5
def div(x):
    if x%3==0:
        return 1
# list1=[11,23,4,5,6,1,10]
# list2=list(filter(greater5,list1))
list1=list(filter(div,range(31)))
print(list1)