import random

poteri = ["Fuoco", "Acqua", "Aria", "Terra", "Cristallo", "Mente", "Luce", "Oscurità", "Vuoto", "Vita", "Ordine", "Realtà"]

def genera_comb_poteri(poteri):
    return random.sample(poteri, 2)
combinazione = genera_comb_poteri(poteri)
print("Combinazione poteri:", combinazione)
