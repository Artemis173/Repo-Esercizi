import random

class Character:
    def __init__(self, name, char_class, hp, strength, dex, intelligence, equipment):
        self.name = name
        self.char_class = char_class
        self.hp = hp
        self.strength = strength
        self.dex = dex
        self.intelligence = intelligence
        self.equipment = equipment

aric = Character("Aric", "Guerriero", 20, 15, 10, 8, ["Spada lunga", "Scudo", "Armatura a piastre"])
lyra = Character("Lyra", "Mago", 12, 8, 12, 16, ["Bastone magico", "Mantello", "Libro degli incantesimi"])
finn = Character("Finn", "Ladro", 15, 10, 16, 10, ["Pugnali", "Mantello dell'ombra", "Kit da scasso"])

goblin = Character("Goblin", "Mostro", 8, 8, 12, 6, [])

def roll_dice(sides):
    return random.randint(1, sides)

def combat(attacker, defender):
    roll = roll_dice(20)
    if attacker.char_class == "Guerriero":
        attack_roll = roll + attacker.strength
    elif attacker.char_class == "Mago":
        attack_roll = roll + attacker.intelligence
    elif attacker.char_class == "Ladro":
        attack_roll = roll + attacker.dex
    else:
        attack_roll = roll
    
    if attack_roll > 10:  
        damage = roll_dice(8)
        defender.hp -= damage
        print(f"{attacker.name} attacca {defender.name} e infligge {damage} danni!")
    else:
        print(f"{attacker.name} attacca {defender.name} ma manca!")

print("Inizio del combattimento:")
combat(aric, goblin)
combat(goblin, aric)

def search_artifact(character):
    roll = roll_dice(20)
    if roll + character.intelligence > 15:
        print(f"{character.name} trova l'artefatto magico!")
    else:
        print(f"{character.name} non riesce a trovare l'artefatto.")

print("Ricerca dell'artefatto:")
search_artifact(lyra)
search_artifact(finn)

def print_character_status(character):
    print(f"{character.name}: HP: {character.hp}, Equipaggiamento: {', '.join(character.equipment)}")

print("Stato finale dei personaggi:")
print_character_status(aric)
print_character_status(finn)
print_character_status(goblin)

print_character_status(lyra)
print_character_status(finn)  