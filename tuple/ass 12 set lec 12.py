n=int(int(input("enter n:")))
d={}
for i in range(n):
    roll_no=int(input("input the roll number"))
    name=input("enter the name")
    markes=int(input("enter the markes"))
    d[roll_no]=[name,markes]
for k in d:
    if(d[k][1]>=75):
        print(d[k][0])
