def reverse (str):
    newstring=""
    for i in str:
        newstring=i+newstring
    print("reverse string is a ",newstring)
str=input("enter a string")
reverse(str)


