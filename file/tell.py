f1=open("sourik.txt","r")
print(f1.read(10))
print("your current location::",f1.tell())
f1.seek(10)
print(f1.read())
f1.close