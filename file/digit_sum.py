f1=open("digit","r")
text=f1.read()
sum=0
p=str(text)
for i in text:
    if text.isdigit:
        for number in text:
            sum=sum+int(number)
            print("sum is=",sum)
f1.close()