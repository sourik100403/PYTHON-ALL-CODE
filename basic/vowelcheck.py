ch=input("enter a charecter :")
vowel=['a','e','i','o','u','A','E','I','O','U']
special=['@','#','$','&']
space=[' ']
digit=[0,1,2,3,4,5,6,7,8,9]
if(ch in vowel):
    print(ch,"is a vowel")
elif(ch in special):
    print(ch,"is a special charecter")
elif(ch in space):
    print(ch,'is a space')
elif(ch in digit):
    print(ch,"is a digit")
else:
    print(ch,"a other charecter")