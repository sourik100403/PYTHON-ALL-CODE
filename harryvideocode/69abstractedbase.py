from abc import ABCMeta , abstractmethod
class shape(ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0
class rectangle(shape):
    type="rectangle"
    side=4
    def __init__(self):
        self.length=6
        self.breath=7
    def printarea(self):
        return  self.length * self.breath
rec1=rectangle()
print(rec1.printarea())

# from abc import ABCMeta, abstractmethod
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def printarea(self):
#         return 0
#
# class Rectangle(Shape):
#     type = "Rectangle"
#     sides = 4
#     def __init__(self):
#         self.length = 6
#         self.breadth = 7
#
#     def printarea(self):
#         return self.length * self.breadth
#
# rect1 = Rectangle()
# print(rect1.printarea())

