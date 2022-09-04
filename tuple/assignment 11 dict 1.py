keys=["ten","twenty","thirty"]
values=[10,20,30]
res_dict=dict()
for i in range(len(keys)):
    res_dict.update({keys[i]:values[i]})
print(res_dict)