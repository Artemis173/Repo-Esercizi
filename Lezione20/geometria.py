from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def render(self):
        pass


class Quadrato(Forma):
    def __init__(self, lato):
        super().__init__("Quadrato")
        self.lato = lato
    
    def getArea(self):
        return self.lato ** 2
    
    def render(self):
        for i in range(self.lato):
            for j in range(self.lato):
                if i == 0 or i == self.lato - 1 or j == 0 or j == self.lato - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        super().__init__("Rettangolo")
        self.base = base
        self.altezza = altezza
    
    def getArea(self):
        return self.base * self.altezza
    
    def render(self):
        for i in range(self.altezza):
            for j in range(self.base):
                if i == 0 or i == self.altezza - 1 or j == 0 or j == self.base - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()

class Triangolo(Forma):
    def __init__(self, lato):
        super().__init__("Triangolo")
        self.lato = lato
    
    def getArea(self):
        return (self.lato ** 2) / 2
    
    def render(self):
        for i in range(self.lato):
            for j in range(i + 1):
                if i == self.lato - 1 or j == 0 or j == i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()


quadrato = Quadrato(5)
print(f"Area del quadrato: {quadrato.getArea}")
quadrato.render()

rettangolo =  Rettangolo(6, 4)
print(f"Area del rettangolo: {rettangolo.getArea}")
rettangolo.render()

triangolo = Triangolo(5)
print(f"Area del triangolo: {triangolo.getArea}")
triangolo.render()