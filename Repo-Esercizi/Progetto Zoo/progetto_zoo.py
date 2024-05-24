class Zoo:
    def __init__(self):
        self.fences = []
        self.zoo_keepers = []

    def feed(self):
        for fence in self.fences:
            for animal in fence.animals:
                if fence.area_remaining >= (animal.height * 1.02) * (animal.width * 1.02):
                    animal.feed()

    def clean(self):
        total_cleaning_time = 0
        for fence in self.fences:
            total_cleaning_time += fence.clean()
        return total_cleaning_time

    def describe_zoo(self):
        print("Guardiani dello zoo:")
        for zoo_keeper in self.zoo_keepers:
            print(f"Nome: {zoo_keeper.name}, Cognome: {zoo_keeper.surname}, ID: {zoo_keeper.id}")

        print("\nRecinti dello zoo:")
        for fence in self.fences:
            print(f"Area: {fence.area}, Temperatura: {fence.temperature}, Habitat: {fence.habitat}")
            print("Animali nel recinto:")
            for animal in fence.animals:
                print(f"Nome: {animal.name}, Specie: {animal.species}, Età: {animal.age}, Salute: {animal.health}")

class Animal:
    def __init__(self, name, species, age, height, width, preferred_habitat):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)

    def feed(self):
        self.health += 1
        self.height *= 1.02
        self.width *= 1.02

class Fence:
    def __init__(self, area, temperature, habitat):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []

    def area_remaining(self):
        used_area = sum(animal.height * animal.width for animal in self.animals)
        return self.area - used_area

    def clean(self):
        if self.area_remaining == 0:
            return self.area
        return sum(animal.height * animal.width for animal in self.animals) / self.area_remaining

class ZooKeeper:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal, fence):
        if fence.area_remaining >= animal.height * animal.width:
            fence.animals.append(animal)
        else:
            print("Non c'è spazio sufficiente nel recinto.")

    def remove_animal(self, animal, fence):
        fence.animals.remove(animal)