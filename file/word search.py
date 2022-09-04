f1=open("char","r")
text=f1.read()
string=str(input("enter the search word ::"))
if string in text:
    print("found")
else:
    print("not found")
f1.close()