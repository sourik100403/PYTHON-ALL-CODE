text=input("enter a string")
length=len(text)
flag=true
for i in range(0,length//2):
    if text[i]!=text[length-1-i]:
        flag=false
        break
if flag==true:
     print("string is palindrom")
else:
    print("string is not palindrom")


