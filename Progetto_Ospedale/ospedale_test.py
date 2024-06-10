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
        self.patients: list[Paziente] = patients
        self.doctor: Dottore = doctor

    def calculateSalary(self):
        return self.doctor.fee * len(self.patients)

    def getInvoiceCount(self):
        return len(self.patients)

    def addPatient(self, patient):
        self.patients.append(patient)

    def removePatient(self, patient):
        self.patients.remove(patient)


import unittest
from ospedale_test import Persona, Dottore, Paziente, Fattura

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona = Persona("Mario", "Rossi")

    def test_initialization(self):
        self.assertEqual(self.persona.first_name, "Mario")
        self.assertEqual(self.persona.last_name, "Rossi")
        self.assertEqual(self.persona.age, 0)

    def test_setName(self):
        self.persona.setName("Luigi")
        self.assertEqual(self.persona.first_name, "Luigi")

    def test_setLastName(self):
        self.persona.setLastName("Bianchi")
        self.assertEqual(self.persona.last_name, "Bianchi")

    def test_setAge(self):
        self.persona.setAge(35)
        self.assertEqual(self.persona.age, 35)

class TestDottore(unittest.TestCase):
    def setUp(self):
        self.dottore = Dottore("Giovanni", "Verdi", "Cardiologia", 150)

    def test_initialization(self):
        self.assertEqual(self.dottore.first_name, "Giovanni")
        self.assertEqual(self.dottore.last_name, "Verdi")
        self.assertEqual(self.dottore.specialization, "Cardiologia")
        self.assertEqual(self.dottore.fee, 150)

    def test_isValidDoctor(self):
        self.dottore.setAge(30)
        self.assertTrue(self.dottore.isValidDoctor())
        self.dottore.setAge(24)
        self.assertFalse(self.dottore.isValidDoctor())
        self.dottore.setAge(71)
        self.assertFalse(self.dottore.isValidDoctor())

class TestPaziente(unittest.TestCase):
    def setUp(self):
        self.paziente = Paziente("Luca", "Neri", "P12345")

    def test_initialization(self):
        self.assertEqual(self.paziente.first_name, "Luca")
        self.assertEqual(self.paziente.last_name, "Neri")
        self.assertEqual(self.paziente.patient_id, "P12345")

class TestFattura(unittest.TestCase):
    def setUp(self):
        self.doctor = Dottore("Anna", "Bianchi", "Dermatologia", 200)
        self.paziente1 = Paziente("Paolo", "Gialli", "P123")
        self.paziente2 = Paziente("Sara", "Blu", "P124")
        self.fattura = Fattura([self.paziente1, self.paziente2], self.doctor)

    def test_initialization(self):
        self.assertEqual(len(self.fattura.patients), 2)
        self.assertEqual(self.fattura.doctor.first_name, "Anna")

    def test_calculateSalary(self):
        self.assertEqual(self.fattura.calculateSalary(), 400)

    def test_getInvoiceCount(self):
        self.assertEqual(self.fattura.getInvoiceCount(), 2)

    def test_addPatient(self):
        new_patient = Paziente("Marco", "Rossi", "P125")
        self.fattura.addPatient(new_patient)
        self.assertIn(new_patient, self.fattura.patients)

    def test_removePatient(self):
        self.fattura.removePatient(self.paziente1)
        self.assertNotIn(self.paziente1, self.fattura.patients)

if __name__ == '__main__':
    unittest.main()