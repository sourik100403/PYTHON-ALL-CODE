text=input("enter a string")
for i in range(0,9):
    newtext=text[i:]+text[:i]
    print(newtext)