class Employee:
    no_of_leave=8
Harry=Employee
Rohan=Employee
Harry.name="Harry"
Harry.age=25
Harry.salary=87676
Rohan.name="Rohan"
Rohan.age=34
Rohan.salary=67635
print(Harry.name)
print(Rohan.salary)
print(Harry.no_of_leave)
print(Rohan.no_of_leave)
print(Employee.no_of_leave)
Harry.no_of_leave=10
print(Harry.no_of_leave)
print(Employee.no_of_leave)

print(Employee.no_of_leave)
print(Employee.__dict__)
Employee.no_of_leave = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)
