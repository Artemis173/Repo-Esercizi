class Persona:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def setName(self, first_name):
        self.first_name = first_name

    def setLastName(self, last_name):
        self.last_name = last_name

    def setAge(self, age):
        self.age = age


class Dottore(Persona):
    def __init__(self, first_name, last_name, specialization, fee):
        super().__init__(first_name, last_name)
        self.specialization = specialization
        self.fee = fee

    def isValidDoctor(self):
        return self.age >= 25 and self.age <= 70


class Paziente(Persona):
    def __init__(self, first_name, last_name, patient_id):
        super().__init__(first_name, last_name)
        self.patient_id = patient_id


class Fattura:
    def __init__(self, patients, doctor):
        self.patients = patients
        self.doctor = doctor

    def calculateSalary(self):
        return self.doctor.fee * len(self.patients)

    def getInvoiceCount(self):
        return len(self.patients)

    def addPatient(self, patient):
        self.patients.append(patient)

    def removePatient(self, patient):
        self.patients.remove(patient)