"""
print A DICCENARY THE KEYS AND NUMBER BETWWN M TO N FOR THEIR VALUS SQURE
"""
m=int(input("enter the first number"))
n=int(input("enter the first number"))
d=dict()
for x in range(m,n+1):
    d[x]=x**2
print(d)