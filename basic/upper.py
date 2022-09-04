ch=input("enter a character :")
if(ch.islower()):
    print(ch.upper())
elif(ch.isupper()):
    print(ch.lower())
else:
    print("it is not a alphabet")