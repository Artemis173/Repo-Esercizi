class Prodotto:
    def init(self, nome: str, quantità: int):
        self.nome = nome
        self.quantità = quantità

class Magazzino:
    def init(self):
        self.prodotti = []

    def aggiungiprodotto(self, prodotto: Prodotto):
        for p in self.prodotti:
            if p.nome == prodotto.nome:
                p.quantità += prodotto.quantità
                return
        self.prodotti.append(prodotto)

    def cercaprodotto(self, nome: str) -> Prodotto:
        for prodotto in self.prodotti:
            if prodotto.nome == nome:
                return prodotto
        return None

    def verificadisponibilità(self, nome: str) -> str:
        prodotto = self.cercaprodotto(nome)
        if prodotto is not None:
            if prodotto.quantità > 0:
                return f"Il prodotto '{nome}' è disponibile con quantità: {prodotto.quantità}."
            else:
                return f"Il prodotto '{nome}' non è disponibile."
        else:
            return f"Il prodotto '{nome}' non esiste nel magazzino."