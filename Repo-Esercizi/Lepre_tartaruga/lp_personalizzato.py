import random

def print_race(positions, hare_pos, tortoise_pos):
    for i in range(70):
        if i == hare_pos and i == tortoise_pos:
            print("OUCH!!!", end=" ")
        elif i == hare_pos:
            print("H", end=" ")
        elif i == tortoise_pos:
            print("T", end=" ")
        else:
            print("_", end=" ")
    print()

def tortoise_move(weather):
    move = random.randint(1, 10)
    if weather == "pioggia":
        move -= 1
    if move <= 5:
        return 3
    elif move <= 7:
        return -6
    else:
        return 1

def hare_move(weather):
    move = random.randint(1, 10)
    if weather == "pioggia":
        move -= 2
    if move <= 2:
        return 0
    elif move <= 4:
        return 9
    elif move <= 5:
        return -12
    elif move <= 8:
        return 1
    else:
        return -2

def change_weather(tick):
    if tick % 10 == 0:
        return random.choice(["soleggiato", "pioggia"])
    else:
        return None

def simulate_race():
    hare_position = 0
    tortoise_position = 0
    tick = 0
    weather = "soleggiato"

    while True:
        tick += 1
        weather = change_weather(tick)
        hare_position += hare_move(weather)
        if hare_position < 0:
            hare_position = 0
        tortoise_position += tortoise_move(weather)
        if tortoise_position < 0:
            tortoise_position = 0
        print_race(70, hare_position, tortoise_position)

        if hare_position >= 70 and tortoise_position >= 70:
            return "tie"
        elif hare_position >= 70:
            return "hare"
        elif tortoise_position >= 70:
            return "tortoise"

def simulate_rounds(num_rounds):
    hare_wins = 0
    tortoise_wins = 0
    ties = 0

    for _ in range(num_rounds):
        result = simulate_race()
        if result == "hare":
            hare_wins += 1
        elif result == "tortoise":
            tortoise_wins += 1
        else:
            ties += 1
    print(f"Hare wins: {hare_wins}, Tortoise wins: {tortoise_wins}, Ties: {ties}") 

simulate_rounds(10000) 