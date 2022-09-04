class person:
    no_of_type=2
    def __init__(self,aname,aage,asalary):
        self.name=aname
        self.age=aage
        self.salary=asalary
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_type=newleaves

harry=person("sourik",23,32000)
print(person.no_of_type)
print(harry.no_of_type)
# person.no_of_type=43
# print(harry.no_of_type)
person.change_leaves(76)
print(person.no_of_type)
print(harry.no_of_type)