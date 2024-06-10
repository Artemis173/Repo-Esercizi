
from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, patients: list[Paziente], doctor: Dottore):
        self.__doctor: Dottore
        
        if doctor.isAValidDoctor():
            self.__fatture = len(patients)
            self.__salary = 0
            self.__patients = patients
            self.__doctor = doctor
        else:
            self.__patients = None
            self.__doctor = None
            self.__fatture = None
            self.__salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        if self.__doctor and self.__patients:
            self.__salary = self.__doctor.getParcel() * len(self.__patients)
        return self.__salary

    def getFatture(self):
        if self.__doctor and self.__patients:
            self.__fatture = len(self.__patients)
        return self.__fatture

    def addPatient(self, new_patient: Paziente):
        if self.__doctor and self.__patients is not None:
            self.__patients.append(new_patient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.__doctor.getLastName()} è stato aggiunto il paziente {new_patient.getIdCode()}")

    def removePatient(self, id_code):
        if self.__doctor and self.__patients is not None:
            for patient in self.__patients:
                if patient.getIdCode() == id_code:
                    self.__patients.remove(patient)
                    self.getFatture()
                    self.getSalary()
                    print(f"Alla lista del Dottor {self.__doctor.getLastName()} è stato rimosso il paziente {id_code}")
                    break