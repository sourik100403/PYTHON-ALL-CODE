class A:
    classvar1="i am in class a"
    def __init__(self):
        self.classvar1="I am in class a whith init function"
        self.special="special"
class B(A):
    classvar1="I am in class B"
    def __init__(self):
        self.classvar1="I am in class B whith init function"
        super().__init__()
        print(super().classvar1)

a=A()
b=B()
print(b.classvar1)
print(b.special)
# print(b.special)

class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)
