class Employee:
    var=10
    no_of_leave=12
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
    def printall(self):
        print(f"the name is {self.name}, salary is {self.salary} age is {self.age}")
    @classmethod
    def from_th(cls,newleaves):
        cls.no_of_leave=newleaves
    @classmethod
    def details(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def stat(string):
        print("this is good",string)
class player:
    # var=9
    no_of_game=4
    def __init__(self,name,game):
        self.name=name
        self.game=game
    def playerdetails(self):
        return f"name is {self.name} game is {self.game}"
class programmer(Employee,player):
    language="c++"
    def printlanguage(self):
        print(self.language)

harry=Employee("harry",878765,87)
rohan=player("rohan",["cricket",'football'])
print(harry.name)
print(Employee.no_of_leave)
harry.printall()
harry.from_th(87)
print(rohan.name)
print(rohan.game)
print(rohan.playerdetails())
print(rohan.no_of_game)
print(Employee.no_of_leave)
print(harry.no_of_leave)
harry=programmer("harry",8867,34)
# rohan=programmer("rohan",["cricket","football"])
# print(harry.printall())
print(Employee.var)
print(player.var)
print(programmer.var)

