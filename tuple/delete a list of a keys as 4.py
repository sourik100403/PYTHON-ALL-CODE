sample_dict={"name":"kelly","age":25,"salary":"8000","city":"new york"}
keys=["name","salary"]
for k in keys:
    sample_dict.pop(k)
sample_dict={"a":100,"b":200,"c":300}
if 200 in sample_dict.value():
    print("200 present in a dict")