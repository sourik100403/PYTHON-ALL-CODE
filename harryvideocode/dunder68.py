class employee:
    no_of_leave=2
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def printdetails(self):
        return f"the name is {self.name} salary is {self.salary} role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leave=newleaves
    def __add__(self, other):
        return self.salary + other.salary
    def __floordiv__(self, other):
        return self.salary // other.salary
    def __truediv__(self, other):
        return self.salary / other.salary
    def __repr__(self):
        return f"the name is ({self.name},{self.salary},{self.role})"
    def __str__(self):
        return f"the name is {self.name} salary is {self.salary} role is {self.role}"
emp1=employee("sourik",540,"programer")
emp2=employee("suraj",5,"cleaner")
print(emp1//emp2)

