f1=open("char","r")
text=f1.read()
f1.close()
f1=open("char","r")
string=str(input("enter the string"))
flag=0
for i in text:
    if string in i:
        flag=flag+1
        break
if flag==0:
    print("string",string,"not found")
else:
    print("string",string,"found")
f1.close()
