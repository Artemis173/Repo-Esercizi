class Animal:
    def __init__(self, name: str):
        self.name = name

    def set_legs(self, legs: str):
        self.legs = legs
    
        
    def get_legs(self) -> int:
        return self.legs
    
    def print_info(self):
        print(f"name: {self.name}, legs: {self.legs}")

Animal_1: Animal = Animal(name = "Canepane")
Animal_1.legs = "4"
Animal_1.print_info()