class A:
    def met(self):
        return ("this is a construtor of class A")
class B(A):
    def met(self):
        return ("this is a construtor of class B")
class C(A):
    def met(self):
        return ("this is a construtor of class C")
class D(C,B):
    def met(self):
        return ("this is a construtor of class D")

a=A()
b=B()
c=C()
d=D()
print(d.met())