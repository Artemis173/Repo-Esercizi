class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = True
    
    def stato_prestito(self):
        return "Disponibile" if self.disponibile else "Non disponibile"


class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)
        return f"Libro '{libro.titolo}' aggiunto al catalogo."

    def presta_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if libro.disponibile:
                    libro.disponibile = False
                    return f"Libro '{titolo}' prestato con successo."
                else:
                    return f"Il libro '{titolo}' non è disponibile al momento."
        return f"Il libro '{titolo}' non è presente nel catalogo."

    def restituisci_libro(self, titolo):
        for libro in self.catalogo:
            if libro.titolo == titolo:
                if not libro.disponibile:
                    libro.disponibile = True
                    return f"Libro '{titolo}' restituito con successo."
                else:
                    return f"Il libro '{titolo}' non è stato prestato."
        return f"Il libro '{titolo}' non è presente nel catalogo."

    def mostra_libri_disponibili(self):
        libri_disponibili = [libro.titolo for libro in self.catalogo if libro.disponibile]
        if libri_disponibili:
            return "Libri disponibili: " + ", ".join(libri_disponibili)
        else:
            return "Nessun libro disponibile al momento."

biblioteca = Biblioteca()

libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien")
libro2 = Libro("1984", "George Orwell")
biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
print(biblioteca.presta_libro("1984"))
print(biblioteca.presta_libro("1984"))
print(biblioteca.presta_libro("Il Signore degli Anelli"))
print(biblioteca.restituisci_libro("1984"))
print(biblioteca.restituisci_libro("Il Signore degli Anelli"))
print(biblioteca.mostra_libri_disponibili())