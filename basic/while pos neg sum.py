#take some number but when it is -1 stop.sum pos and neg value
pos=0
neg=0
print("enter the value but stop at when it is -1")
while(1):
    n=int(input("enter the value :"))
    if(n==-1):
        break
    elif(n>0):
        pos=pos+n
    else:
        neg=neg+n
print("sum of positive value is ::",pos,"sum og negative value is ::",neg)
