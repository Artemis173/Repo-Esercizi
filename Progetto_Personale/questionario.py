def ask_questions(questions):
    answers = []
    for i, question in enumerate(questions, 1):
        print(f"Domanda {i}: {question['question']}")
        for j, option in enumerate(question['options'], 1):
            print(f"  {j}. {option}")
        answer = input("Inserisci il numero della tua risposta: ")
        while not answer.isdigit() or int(answer) < 1 or int(answer) > len(question['options']):
            answer = input("Risposta non valida. Inserisci il numero della tua risposta: ")
        answers.append(int(answer))
    return answers

def calculate_result(answers, results):
    result_key = tuple(answers)
    return results.get(result_key, "Risultato sconosciuto")

def main():
    questions = [
        {
            "question": "Qual è il tuo colore preferito?",
            "options": ["Rosso", "Blu", "Verde", "Giallo"]
        },
        {
            "question": "Qual è il tuo animale preferito?",
            "options": ["Cane", "Gatto", "Leone", "Elefante"]
        },
        {
            "question": "Qual è la tua stagione preferita?",
            "options": ["Inverno", "Primavera", "Estate", "Autunno"]
        }
    ]

    # Definire i risultati per combinazioni di risposte
    results = {
        (1, 1, 1): "Sei una persona energica e passionale.",
        (2, 2, 2): "Sei una persona calma e riflessiva.",
        (3, 3, 3): "Sei una persona avventurosa e curiosa.",
        (4, 4, 4): "Sei una persona calda e accogliente.",
        # Aggiungere altre combinazioni e risultati qui
    }

    print("Benvenuto al questionario!\n")
    answers = ask_questions(questions)
    result = calculate_result(answers, results)
    print(f"\nIl tuo risultato è: {result}")

if __name__ == "__main__":
    main()