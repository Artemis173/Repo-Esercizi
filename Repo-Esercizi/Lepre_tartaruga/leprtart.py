import random

def print_race(positions, hare_pos, tortoise_pos):
    for i in range(1, 71):
        if i == hare_pos and i == tortoise_pos:
            print("OUCH!!!", end=" ")
        elif i == hare_pos:
            print("H", end=" ")
        elif i == tortoise_pos:
            print("T", end=" ")
        else:
            print(i, end=" ")
    print()

def tortoise_move(weather, energy):
    move = random.randint(1, 10)
    if weather == "pioggia":
        move -= 1
    if move <= 5:  # Passo veloce
        if energy >= 5:
            energy -= 5
            return 3, energy
        else:
            energy += 10
            return 0, energy
    elif move <= 7:  # Scivolata
        if energy >= 10:
            energy -= 10
            return -6, energy
        else:
            energy += 10
            return 0, energy
    else:  # Passo lento
        if energy >= 3:
            energy -= 3
            return 1, energy
        else:
            energy += 10
            return 0, energy

def hare_move(weather, energy):
    move = random.randint(1, 10)
    if weather == "pioggia":
        move -= 2
    if move <= 2:  # Riposo
        energy = min(100, energy + 10)
        return 0, energy
    elif move <= 4:  # Grande balzo
        if energy >= 15:
            energy -= 15
            return 9, energy
        else:
            energy += 10
            return 0, energy
    elif move == 5:  # Grande scivolata
        if energy >= 20:
            energy -= 20
            return -12, energy
        else:
            energy += 10
            return 0, energy
    elif move <= 8:  # Piccolo balzo
        if energy >= 5:
            energy -= 5
            return 1, energy
        else:
            energy += 10
            return 0, energy
    else:  # Piccola scivolata
        if energy >= 8:
            energy -= 8
            return -2, energy
        else:
            energy += 10
            return 0, energy

def change_weather(tick):
    if tick % 10 == 0:
        return random.choice(["soleggiato", "pioggia"])
    else:
        return None

def apply_obstacles(position, obstacoles):
    if position in obstacoles:
        return position + obstacoles[position]
    return position

print("BANG !!!!! AND THEY'RE OFF !!!!!")

hare_position = 0
tortoise_position = 0
hare_energy = 100
tortoise_energy = 100

tick = 0
weather = "soleggiato"

obstacoles = {15: -3, 30: -5, 45: -7}
bounces = {10: 5, 25: 3, 50: 10}

while True:           
    tick += 1
    weather = change_weather(tick) or weather  # Keep current weather if None

    hare_move_result, hare_energy = hare_move(weather, hare_energy)
    hare_position += hare_move_result
    if hare_position < 0:
        hare_position = 0
    hare_position = apply_obstacles(hare_position, obstacoles)
    hare_position = apply_obstacles(hare_position, bounces)
    
    tortoise_move_result, tortoise_energy = tortoise_move(weather, tortoise_energy)
    tortoise_position += tortoise_move_result
    if tortoise_position < 0:
        tortoise_position = 0
    tortoise_position = apply_obstacles(tortoise_position, obstacoles)
    tortoise_position = apply_obstacles(tortoise_position, bounces)

    print_race(70, hare_position, tortoise_position)

    if hare_position >= 70 and tortoise_position >= 70:
        print("IT'S A TIE.")
        break
    elif hare_position >= 70:
        print("HARE WINS! YUCH!!!")
        break
    elif tortoise_position >= 70:
        print("TORTOISE WINS! VAY!!!")
        break 