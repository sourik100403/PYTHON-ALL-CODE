# f=open("32harry")
# print(f.readlines())
# f.close()
with open("32harry") as f:
    a=f.readlines()
    print(a)
f=open("32harry")
print(f.read())
f.close()