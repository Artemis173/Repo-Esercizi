# driver.py

from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

doctor1 = Dottore("Mario", "Rossi", "Pediatra", 100.0)
doctor2 = Dottore("Luigi", "Verdi", "Ostetrico", 150.0)

doctor1.setAge(40)
doctor2.setAge(35)

doctor1.doctorGreet()
doctor2.doctorGreet()

patient1 = Paziente("Anna", "Bianchi", "P1")
patient2 = Paziente("Giulia", "Neri", "P2")
patient3 = Paziente("Luca", "Rossi", "P3")
patient4 = Paziente("Marco", "Verdi", "P4")


patients_list1 = [patient1, patient2, patient3]
patients_list2 = [patient4]

fattura1 = Fattura(patients_list1, doctor1)
fattura2 = Fattura(patients_list2, doctor2)

print(f"Salario Dottore1: {fattura1.getSalary()} euro!")
print(f"Salario Dottore2: {fattura2.getSalary()} euro!")

fattura1.removePatient("P2")
fattura2.addPatient(patient2)

print(f"Salario Dottore1: {fattura1.getSalary()} euro!")
print(f"Salario Dottore2: {fattura2.getSalary()} euro!")

total_earnings = fattura1.getSalary() + fattura2.getSalary()
print(f"In totale, l'ospedale ha incassato: {total_earnings} euro!")