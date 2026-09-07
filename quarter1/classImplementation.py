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

David = Employee("David", 34, 10000, "Finance")
Natalia = Employee("Natalia", 41, 15000, "Creatives")

print("David's initial attributes: ")
David.displayInfo()
print("Natalia's initial attributes: ")
Natalia.displayInfo()

Natalia.updateDepartment("Publication")

print("David's final attributes: ")
David.displayInfo()
print("Natalia's final attributes: ")
Natalia.displayInfo()
