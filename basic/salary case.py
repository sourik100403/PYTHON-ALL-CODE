a=int(input("enter a salary :"))
if(a<10000):
    bouns=a*.2
elif(a>10000 and a<20000):
    bouns=a*.05
else:
    bouns=a*.02
sal=a+bouns
print("total salary is ",sal)
