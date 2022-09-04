# l=10
# def sum(n):
#     global l
#     l=5+l
#     m=9
#     print(l,m)
#     print(n,"i have printed")
# sum("sourik")
# print(l)
x=98
def harry():
    x=20
    def rohan():
        global x
        x=88
    print("beforore call rohan()",x)
    rohan()
    print("after calling rohan()",x)
harry()
print(x)