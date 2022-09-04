# class person:
#     no_of_type=2
#     pass
#     def printout(self):
#         return f"the name {self.name} ,age {self.age} , salary{self.salary} , wife name {self.wife} "
# harry=person()
# rohan=person()
#
# harry.name="sourik"
# harry.age=19
# harry.salary=12000
# harry.wife="sritikona"
#
#
# rohan.name="suraj"
# rohan.age=17
# rohan.salary=14500
# rohan.wife="priya"
#
#
# print(harry.printout())
# print(rohan.printout())
# print(person.no_of_type)
# print(harry.no_of_type)
# print(rohan.no_of_type)
# print(rohan.__dict__)

#////****__init__ function
class person:
    no_of_type=2
    def __init__(self,aname,aage,asalary):
        self.name=aname
        self.age=aage
        self.salary=asalary
harry=person("sourik",23,32000)
print(harry.name)
print(harry.age)
print(harry.salary)