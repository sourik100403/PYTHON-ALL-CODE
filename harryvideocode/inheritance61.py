class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class programme(Employee):
    no_of_holiday =67
    def __init__(self, aname, asalary, arole,language):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language=language
    def printall(self):
        return (f"name is{self.name},salary is{self.salary},role is{self.role},language={self.language}")

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = programme("Shubham", 555, "Programmer", ["python"])
karan = programme("Karan", 777, "Programmer", ["python", "Cpp"])
print(karan.no_of_holiday)
print(harry.printdetails())
