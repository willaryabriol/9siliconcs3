class Patient:

    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount

    @property
    def name(self):
        print(f"Patient Name: {self._name}")

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def bill(self):
        print(f"Original Bill: {self._bill_amount}")
        print(f"Final Bill: {self.calculate_bill}")

    @bill.setter
    def bill(self, bill_amount):
        self._bill_amount = bill_amount

    def calculate_bill(self): #first method to be overridden
        return self._bill_amount

    @property
    def display_patient_type(self): #second method to be overridden
        print("Patient Type: Regular Patient")

class SeniorPatient(Patient):

    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self): #overrides the calculate_bill of parent class
        bill_amount = bill_amount * 0.8
        return self._bill_amount

    @property
    def display_patient_type(self): #overrides the display patient type of parent class
        print("Senior Citizen")

class PhilHealthPatient(Patient):

    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self): #overrides the calculate_bill of parent class
        bill_amount = bill_amount * 0.85
        return self._bill_amount

    @property
    def display_patient_type(self): #overrides the display patient type of parent class
        print("PhilHealth Member")

#setting the values
regular = Patient("Juan Dela Cruz", 15000)
senior = SeniorPatient("Maria Santos", 15000)
philhealth = PhilHealthPatient("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-----------------------")
regular.name
regular.display_patient_type
regular.bill
print()
senior.name
senior.display_patient_type
senior.bill
print()
philhealth.name
philhealth.display_patient_type
philhealth.bill
