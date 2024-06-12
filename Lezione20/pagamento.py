
# Si definisca una nuova classe Pagamento che contiene un attributo privato e di tipo float che memorizza l'importo del pagamento 
# e si definiscano appropriati metodi get() e set(). L'importo non è un parametro da passare in input alla classe Pagamento 
# ma deve essere inizializzato utilizzando il metodo set() dove opportuno. 
# Si crei inoltre un metodo dettagliPagamento() che visualizza una frase che descrive l'importo del pagamento,
# ad esempio: "Importo del pagamento: €20.00". Quando viene stampato, l'importo è sempre con 2 cifre decimali.

# Successivamente, si definisca una classe PagamentoContanti che sia derivata da Pagamento e definisca l'importo. 
# Questa classe dovrebbe ridefinire il metodo dettagliPagamento() per indicare che il pagamento è in contanti. 
# Si definisca inoltre il metodo inPezziDa() che stampa a schermo quante banconote da 500 euro, 200 euro, 100 euro, 50 euro, 20 euro, 
# 10 euro, 5 euro e/o in quante monete da 2 euro, 1 euro, 0,50 euro, 0,20 euro, 0,10 euro, 0,05 euro, 0,01 euro sono necessarie 
# per pagare l'importo in contanti.

# Si definisca una classe PagamentoCartaDiCredito derivata anch'essa da Pagamento e che definisce l'importo. 
# Questa classe deve contenere gli attributi per il nome del titolare della carta, la data di scadenza, 
# e il numero della carta di credito. Infine, si ridefinisca il metodo dettagliPagamento() per includere 
# tutte le informazioni della carta di credito oltre all'importo del pagamento.

# Per il test, si creino almeno due oggetti di tipo PagamentoContanti e due di tipo PagamentoCartaDiCredito con valori differenti 
# e si invochi dettagliPagamento() per ognuno di essi.

# Esempio di output:
# Pagamento in contanti di: €150.00
# 150.00 euro da pagare in contanti con:
# 1 banconota da 100 euro
# 1 banconota da 50 euro

# Pagamento in contanti di: €95.25
# 95.25 euro da pagare in contanti con:
# 1 banconota da 50 euro
# 2 banconote da 20 euro
# 1 banconota da 5 euro
# 1 moneta da 0.2 euro
# 1 moneta da 0.05 euro

# Pagamento di: €200.00 effettuato con la carta di credito
# Nome sulla carta: Mario Rossi
# Data di scadenza: 12/24
# Numero della carta: 1234567890123456

# Pagamento di: €500.00 effettuato con la carta di credito
# Nome sulla carta: Luigi Bianchi
# Data di scadenza: 01/25
# Numero della carta: 6543210987654321


class Pagamento:
    def __init__(self):
        self.__importo: float = 0.0

    def get(self):
        return self.__importo
    
    def set(self, importo: float):
        self.__importo = importo

    def dettagliPAgamento(self):
        importo_formattato = "{:.2f}".format(self.__importo)
        print(f"L'importo del pagamento è:  €{importo_formattato}")


class PagamentoContanti(Pagamento):
    def __init__(self):
        super().__init__()

    def dettagliPagamento(self):
        importo = self.get()
        print(f"L'importo del pagamento è: €{importo:.2f}")

    def inPezziDa(self):
        importo = self.get()
        pezzi = {
            500: 0,
            200: 0,
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            2: 0,
            1: 0,
            0.5: 0,
            0.2: 0,
            0.1: 0,
            0.05: 0,
            0.01: 0
        }

        for valore in pezzi:
            if importo >= valore:
                pezzi[valore] = int(importo // valore)
                importo -= pezzi[valore] * valore

        for valore, quantita in pezzi.items():
            if quantita > 0:
                print(f"{quantita} pezzi da {valore} euro")


class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, titolare, scadenza, numero):
        super().__init__()
        self.__titolare = titolare
        self.__scadenza = scadenza
        self.__numero = numero

    def dettagliPagamento(self):
        print(f"Pagamento in contanti:\n"
              f"€{self.get():.2f}\n"
              f"Titolare: {self.__titolare}\n"
              f"Scadenza: {self.__scadenza}\n"
              f"Numero: {self.__numero}")


pagamento1 = PagamentoContanti()
pagamento1.set(150.00)
pagamento1.dettagliPagamento()
print()
pagamento2 = PagamentoContanti()
pagamento2.set(95.25)
pagamento2.dettagliPagamento()
print()
pagamento3 = PagamentoCartaDiCredito("Mario Rossi", "12/24", "1234567890123456")
pagamento3.set(200.00)
pagamento3.dettagliPagamento()
print()
pagamento4 = PagamentoCartaDiCredito("Luigi Bianchi", "01/25", "6543210987654321")
pagamento4.set(500.00)
pagamento4.dettagliPagamento()