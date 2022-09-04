text=input("enter a string")
upper=lower=digit=space=0
for i in text:
    if(i.islower()):
        lower+=1
    elif(i.isupper()):
        upper+=1
    elif(i.isdigit()):
        digit+=1
    elif(i.isspace()):
        space+=1
print("number of uppercase",upper)
print("number of lowercase",lower)
print("number of digit",digit)
print("number of space",space)