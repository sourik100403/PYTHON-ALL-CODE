"""age=int(input("enter your age :"))
if(age==18):
    print("driving is your choice")
elif(age>18):
    print("you can drive")
else:
    print("you can not drive")
"""
age=int(input("enter your age :"))
if(age>=18 and age<=65):
    print("you can drive")
elif(age<18):
    print("you can not eligible for drive")
else:
    print("you can not drive")