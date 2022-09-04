list1=[12,15,11,12,8,15,3,3]
res_list=[]
for i in list1:
    if i not in res_list:
        res_list.append(i)
print(res_list)