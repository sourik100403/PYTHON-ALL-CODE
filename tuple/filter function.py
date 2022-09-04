def is_negative(x):
    if(x<0):
        return x
list1=[-12,-14,-54,76,76,98]
list2=[]
list2=list(filter(is_negative,list1))
print("the negtive value is",list2)
