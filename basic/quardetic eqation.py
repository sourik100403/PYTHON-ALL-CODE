import math
a=int(input("enter the first number :"))
b=int(input("enter the second number :"))
c=int(input("enter the third number :"))
d=(b*b)-(4*a*c)
if(d>0):
    print("it is real root")
    root1=(-b+math.sqrt(d))/(2*a)
    root2 = (-b-math.sqrt(d)) / (2 * a)
    print("root1:",round(root1,2),"root2:",round(root2,2))
elif(d==0):
    print("it is a equal root ")
    root1=b/(2*a)
    print("root1:", round(root1, 2), "root2:", round(root1, 2))
else:
    print("it is imagency")
