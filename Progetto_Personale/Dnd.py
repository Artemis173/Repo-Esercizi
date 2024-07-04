import random
# Definizione delle classi dei personaggi
class Character:
    def __init__(self, name, char_class, hp, strength, dex, intelligence, equipment, gold):
        self.name = name
        self.char_class = char_class
        self.hp = hp
        self.strength = strength
        self.dex = dex
        self.intelligence = intelligence
        self.equipment = equipment
        self.gold = 0

    def heal(self):
        heal_amount = random.randint(5, 15)
        self.hp += heal_amount
        print(f"{self.name} si è curato e ora ha {self.hp} HP.")

    def full_heal(self):
        self.hp = 20  # Supponiamo che 20 sia il massimo HP
        print(f"{self.name} è completamente guarito e ora ha {self.hp} HP.")

    def add_gold(self, amount):
        self.gold += amount
        print(f"{self.name} ha acquisito {amount} oro e ora ha {self.gold} oro.")

# Definizione della classe dei mostri
class Monster:
    def __init__(self, name, hp, strength, dex, intelligence, equipment):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.dex = dex
        self.intelligence = intelligence
        self.equipment = equipment

# Creazione dei mostri
def create_monster():
    monsters = [
        ("Goblin Guerriero", 10, 12, 10, 6, ["Spada corta"]),
        ("Goblin Lancieri", 8, 10, 12, 6, ["Lancia"]),
        ("Goblin Arcieri", 6, 8, 14, 6, ["Arco e frecce"]),
        ("Goblin", 8, 8, 12, 6, []),
        ("Goblin Sciamani", 10, 6, 10, 14, ["Bastone magico"]),
        ("Re dei Goblin", 20, 15, 12, 10, ["Spada lunga", "Armatura"])
    ]
    name, hp, strength, dex, intelligence, equipment = random.choice(monsters)
    return Monster(name, hp, strength, dex, intelligence, equipment)

# Creazione dei personaggi
aric = Character("Aric","Guerriero",20,15,10,8,['Spada lunga','Scudo','Armatura a piastre'], 0)
lyra = Character("Lyra","Mago",12,8,12,16,['Bastone magico','Mantello','Libro degli incantesimi'], 0)
finn = Character("Finn","Ladro",15,10,16,10,['Pugnali',"Mantello dell'ombra",'Kit da scasso'], 0)

# Funzione per tirare il dado
def roll_dice(sides):
    return random.randint(1, sides)

# Funzione per il combattimento
def combat(characters, monsters):
    turn = 0
    while characters and monsters:
        attacker = characters[turn % len(characters)] if turn % 2 == 0 else monsters[turn % len(monsters)]
        defender = monsters[turn % len(monsters)] if turn % 2 == 0 else characters[turn % len(characters)]
        
        if attacker.hp > 0 and defender.hp > 0:
            roll = roll_dice(20)
            if isinstance(attacker, Character):
                if attacker.char_class == "Guerriero":
                    attack_roll = roll + attacker.strength
                elif attacker.char_class == "Mago":
                    attack_roll = roll + attacker.intelligence
                elif attacker.char_class == "Ladro":
                    attack_roll = roll + attacker.dex
                else:
                    attack_roll = roll + attacker.strength
            else:
                attack_roll = roll + attacker.strength
            
            if attack_roll > 10:  # Supponiamo che la Classe Armatura (CA) sia 10
                damage = roll_dice(8)
                defender.hp -= damage
                print(f"{attacker.name} attacca {defender.name} e infligge {damage} danni!")
                if defender.hp <= 0:
                    print(f"{defender.name} è stato sconfitto!")
                    if isinstance(defender, Monster):
                        monsters.remove(defender)
                    else:
                        characters.remove(defender)
            else:
                print(f"{attacker.name} attacca {defender.name} ma manca!")
        
        turn += 1
        
        if not monsters:
            print("Tutti i mostri sono stati sconfitti!")
            return True
        elif not characters:
            print("Tutti i personaggi sono stati sconfitti!")
            return False

# Generazione casuale delle stanze
def generate_rooms():
    room_types = ["Stanza vuota", "Stanza del tesoro", "Stanza del mostro", "Stanza di ristoro rapido"]
    rooms = random.choices(room_types, k=12)
    rooms.append("Stanza del tesoro")
    rooms.append("Stanza del mostro con Re dei Goblin")
    rooms.append("Stanza di ristoro rapido")
    random.shuffle(rooms)
    return rooms

# Generazione della mappa 10x10
def generate_map():
    room_types = ["Stanza vuota", "Stanza del tesoro", "Stanza del mostro", "Stanza di ristoro rapido"]
    map_size = 10
    dungeon_map = [[random.choice(room_types) for _ in range(map_size)] for _ in range(map_size)]
    dungeon_map[random.randint(0, 9)][random.randint(0, 9)] = "Stanza del tesoro"
    dungeon_map[random.randint(0, 9)][random.randint(0, 9)] = "Stanza del mostro con Re dei Goblin"
    return dungeon_map

# Esplorazione delle stanze
def explore(characters):
    print("Esplorazione delle stanze:")
    directions = ["sinistra", "destra", "avanti", "indietro"]
    dungeon_map = generate_map()
    explored_rooms = set()
    current_position = (0, 0)
    room_count = 0

    while room_count < 15:
        if current_position in explored_rooms:
            print(f"Sei tornato in una stanza già conquistata.")
            current_position = move_position(current_position, directions)
            continue
        
        room = dungeon_map[current_position[0]][current_position[1]]
        explored_rooms.add(current_position)
        print(f"Sei in una {room}.")
        
        if room == "Stanza del mostro" or room == "Stanza del mostro con Re dei Goblin":
            if room == "Stanza del mostro con Re dei Goblin":
                monster = Monster("Re dei Goblin", 20, 15, 12, 10, ["Spada lunga", "Armatura"])
            else:
                monster = create_monster()
            print(f"Un {monster.name} appare!")
            monsters = [monster]
            if not combat(characters, monsters):
                break
        
        if room == "Stanza di ristoro rapido":
            for character in characters:
                character.full_heal()
            roll = roll_dice(20)
            if roll <= 10:
                print("Sei stato imboscato!")
                monster = create_monster()
                monsters = [monster]
                if not combat(characters, monsters):
                    break
        
        if room == "Stanza del tesoro":
            for character in characters:
                character.add_gold(100)
        
        for character in characters:
            if character.hp < 10:
                heal_decision = input(f"{character.name} ha {character.hp} HP. Vuoi curarti? (s/n): ").lower()
                if heal_decision == 's':
                    character.heal()

        direction = input("In quale direzione vuoi andare? (sinistra/destra/avanti/indietro): ").lower()
        if direction not in directions:
            print("Direzione non valida. Riprova.")
        else:
            current_position = move_position(current_position, direction)
        
        continue_exploring = input("Vuoi continuare ad esplorare? (s/n): ").lower()
        if continue_exploring != 's':
            break
        
        room_count += 1

def move_position(current_position, direction):
    x, y = current_position
    if direction == "sinistra":
        y = max(0, y - 1)
    elif direction == "destra":
        y = min(9, y + 1)
    elif direction == "avanti":
        x = max(0, x - 1)
    elif direction == "indietro":
        x = min(9, x + 1)
    return (x, y)

# Funzione per la ricerca dell'artefatto
def search_artifact(character):
    roll = roll_dice(20)
    if roll + character.intelligence > 15:
        print(f"{character.name} trova l'artefatto magico!")
    else:
        print(f"{character.name} non riesce a trovare l'artefatto.")

# Funzione per stampare lo stato dei personaggi
def print_character_status(character):
    print(f"{character.name}: HP: {character.hp}, Oro: {character.gold}")

# Stato iniziale dei personaggi
print("Stato iniziale dei personaggi:")
print_character_status(aric)
print_character_status(lyra)
print_character_status(finn)

# Simulazione dell'esplorazione
characters = [aric, lyra, finn]
explore(characters)

# Ricerca dell'artefatto
print("Ricerca dell'artefatto:")
search_artifact(aric) 
search_artifact(lyra)
search_artifact(finn)

# Stato finale dei personaggi
print("Stato finale dei personaggi:")
print_character_status(aric)
print_character_status(lyra)
print_character_status(finn)