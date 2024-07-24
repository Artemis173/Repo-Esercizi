def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    merged_dict = dict1.copy()

    for k, v in dict2.items():
        if k in merged_dict:
            merged_dict[k] += v
        else:
            merged_dict[k] = v
    
    return merged_dict  


# Scrivi una funzione che accetti un dizionario di prodotti con i prezzi e restituisca un nuovo dizionario con solo i prodotti che 
# hanno un prezzo superiore a 20, ma scontati del 10%.

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    scontati = {}
    for k, v in prodotti.items():
        if v > 20:
            scontati[k] = v * 0.9
    return scontati


# Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. 
# Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.

def lista_a_dizionario(tuples: tuple) -> dict[str:list[int]]:
    dizionario = {}
    for k, v in tuples:
        if k in dizionario:
            dizionario[k].append(v)
        else:
            dizionario[k] = [v]
    return dizionario


# Scrivi una funzione che prenda un dizionario e un valore, 
# e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.

def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for k, v in dizionario.items():
        if k == valore:
            return k
        else:
            return None


# Scrivi una funzione che prende una lista di numeri e 
# ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.

def classifica_numeri(lista: int) -> dict[str:list[int]]:
    dizionario = {"pari": [], "dispari": []}
    for n in lista:
        if n % 2 == 0:
            if "pari" in dizionario:
                dizionario["pari"].append(n)
        else:
            dizionario["dispari"].append(n)
    return dizionario


# Scrivi una funzione che accetti tre parametri: username, password e status di attivazione dell'account (attivo/non attivo). 
# L'accesso è consentito solo se il nome utente è "admin", la password corrisponde a "12345" e l'account è attivo. 
# La funzione ritorna "Accesso consentito" oppure "Accesso negato".