class Employee:
    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.__salary = salary
        self.__department = department

    def updateSalary(self, amt):
        self.__salary = amt

    def displayInfo(self):
        print(f"{self.name}, {self.age}, {self.__salary}, {self.__department}")

    def updateDepartment(self, dept):
        self.__department = dept

class Supervisor:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def assignEmployee(self, employee):
        self.employees.append(employee)

    def showAssigned(self):
        employees = [str(p) for p in self.employees]
        print(f"Assigned employees to Supervisor {self.name}: {', '.join(employees)}")

s1 = Supervisor("Kylie")
e1 = Employee("Carl", 15, 20, "Creatives")
e2 = Employee("CJ", 21, 15, "Finance")
e3 = Employee("Paris", 13, 12, "Documentation")

s1.assignEmployee(e1)
s1.assignEmployee(e2)
s1.assignEmployee(e3)

s1.showAssigned()



