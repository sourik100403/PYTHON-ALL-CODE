f=open("harry77")
try:
    f1=open("harry77")
except EOFError as s:
    print("this is eoferror",s)
except ZeroDivisionError as s:
    print("this is a zero division error",s)
except IOError as s:
    print("ths is a io error",s)
else:
    print("if except will not run, then else will be run")
finally:
    print("finally always run....... continue")
    f.close()
    f1.close()
print("complete running")
