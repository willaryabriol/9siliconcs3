class Employee:
    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.__salary = salary
        self.__department = department

    def updateSalary(self, amt):
        pass

    def displayInfo(self):
        print(f"{self.name}, {self.age}, {self.__salary}, {self.__department}")

    def updateDepartment(self, dept):
        self.__department = dept

David = Employee("David", 34, 10000, "Finance")
Natalia = Employee("Natalia", 41, 15000, "Creatives")

Natalia.updateDepartment("Publication")

David.displayInfo()
Natalia.displayInfo()
