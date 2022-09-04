''' i/p =wellcome to python class
    o/p= WELLCOME TO PYTHON CLASS'''
str="wellcome to python class"
print(str.upper())
print(str.split())
print('-'.join(str.split()))
print(str.replace("python","java"))
str1=input("enter the stringto find its position:")
print("position of",str1,"is",str.find(str1))