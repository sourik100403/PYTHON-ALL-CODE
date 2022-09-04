# def func1():
#     print("subcribe now")
# func2=func1
# del func1
# func2()


# def funcret(num):
#      if num==0:
#          return print
#      if num==1:
#          return sum
# a=funcret(1)
# print(a)
#
# def exec(func):
#     func("this")
# exec(print)

def dec1(func1):
    def nowexc():
        print("now exceuting")
        func1()
        print("exceuted")
    return nowexc()
#@dec1
def who_is_harry():
    print("harry is good boy")
who_is_harry==dec1(who_is_harry)
