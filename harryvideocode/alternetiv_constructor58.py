class person:
    no_of_type=2
    def __init__(self,aname,aage,asalary):
        self.name=aname
        self.age=aage
        self.salary=asalary
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_type=newleaves
    @classmethod
    def from_change(cls,string):
        param=string.split("-")
        print(param)
        return cls((param[0],param[1],param[2]))
       #return cls(*string.split("-"))
harry=person("sourik",15,77656)
parui=person("papu"-"67"-"7876")
print(harry.name)
print(parui.name)