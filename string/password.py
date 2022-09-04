length=lower=upper=digit=False
password=input("enter a password::")
if len(password)>=8:
    length=True

    for i in password:
        if i.islower():
            lower=True
        elif i.isupper():
            upper=True
        elif i.isdigit():
            digit=True
if(length==lower==upper==digit==True):
    print("password is valid")
else:
    print("password is not valid")