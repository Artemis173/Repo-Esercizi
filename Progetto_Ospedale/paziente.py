
### CLASSE: Paziente
#Creare un file chiamato "paziente.py".
#In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

#Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
#- Definire i seguenti metodi:

#    costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
#    setIdCode(idCode): consente di impostare il codice identificativo del paziente.
#    getidCode(): consente di ritornare il codice identificativo del paziente.
#    patientInfo(): stampa in output le informazioni del paziente in questo modo:

#        "Paziente: {nome} {cognome}
#         ID: {codice identificativo}"

from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name, id_code):
        super().__init__(first_name, last_name)
        if isinstance(id_code, str):
            self.__id_code = id_code
        else:
            self.__id_code = None
            print("Il codice identificativo inserito non è una stringa!")

    def setIdCode(self, id_code):
        if isinstance(id_code, str):
            self.__id_code = id_code
        else:
            print("Il codice identificativo inserito non è una stringa!")

    def getIdCode(self):
        return self.__id_code

    def patientInfo(self):
        print(f"Paziente: {self.getName()} {self.getLastName()}\nID: {self.__id_code}")