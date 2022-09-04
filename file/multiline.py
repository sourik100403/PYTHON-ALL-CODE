f1=open("multiline","w")
print("file name=",f1.name)
list_line=["I am a student"," I study in btech,in durgapur \n"," ece branch"]
f1.writelines(list_line)
f1.close()
print("data save and now read the data")

f1=open("multiline","r")
print(f1.read())
f1.close()

f1=open("multiline","r")
print(f1.readline())
f1.close()