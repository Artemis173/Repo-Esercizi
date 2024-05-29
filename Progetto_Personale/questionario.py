def ask_questions(node, answers, prev_node = None):
    if 'question' not in node:
        return node['result']

    print(node['question'])
    for i, option in enumerate(node['options'], 1):
        print(f"  {i}. {option['text']}")
    answer = input("Inserisci il numero della tua risposta: ")
    while not answer.isdigit() or int(answer) < 1 or int(answer) > len(node['options']):
        answer = input("Risposta non valida. Inserisci il numero della tua risposta: ")

    answer_index = int(answer) - 1
    answers.append(answer_index)
    next_node = node['options'][answer_index]
    

    if 'next' in next_node:
        return ask_questions(next_node['next'], answers, node)
    elif 'result' in next_node:
        return next_node['result']
    else:
        # Se non c'è una domanda successiva e non c'è un risultato, significa che dobbiamo riproporre la domanda
        if next_node['text'].lower() == "no":
            answers.pop()  # Rimuove l'ultima risposta (il "no")
            return ask_questions(prev_node, answers)
        else:
            return ask_questions(next_node, answers)


def calculate_result(answers):
    # Placeholder per la logica del calcolo del risultato finale
    return "Risultato finale basato sulle risposte."

def main():
    # Struttura ad albero delle domande
    question_tree = {
        'question': "Qual è il colore che ti piace di più?",
        'options': [
            {'text': "Rosso", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': {"Hai scelto Rosso"}},
                    {'text': "No"}
                ]
            }},
            {'text': "Giallo", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': {"Hai scelto Giallo"}},
                    {'text': "No"}
                ]
            }},
            {'text': "Blu", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': {"Hai scelto Blu"}},
                    {'text': "No"}
                ]
            }},
            {'text': "Arancio", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'next': {
                        'question': "A quale dei due colori primari che lo compongono ti senti più vicino?",
                        'options': [
                            {'text': "Rosso", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': {"Hai scelto Arancio con preferenza Rosso"}},
                                    {'text': "No"}
                                ]
                            }},
                            {'text': "Giallo", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': {"Hai scelto Arancio con preferenza Giallo"}},
                                    {'text': "No"}
                                ]
                            }}
                        ]
                    }},
                    {'text': "No"}
                ]
            }},
            {'text': "Verde", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'next': {
                        'question': "A quale dei due colori primari che lo compongono ti senti più vicino?",
                        'options': [
                            {'text': "Giallo", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': {"Hai scelto Verde con preferenza Giallo"}},
                                    {'text': "No"}
                                ]
                            }},
                            {'text': "Blu", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': {"Hai scelto Verde con preferenza Blu"}},
                                    {'text': "No"}
                                ]
                            }}
                        ]
                    }},
                    {'text': "No"}
                ]
            }},
            {'text': "Viola", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'next': {
                        'question': "A quale dei due colori primari che lo compongono ti senti più vicino?",
                        'options': [
                            {'text': "Rosso", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': {"Hai scelto Viola con preferenza Rosso"}},
                                    {'text': "No"}
                                ]
                            }},
                            {'text': "Blu", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': {"Hai scelto Viola con preferenza Blu"}},
                                    {'text': "No"}
                                ]
                            }}
                        ]
                    }},
                    {'text': "No"}
                ]
            }},
            {'text': "Bianco", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': {"Hai scelto Bianco"}},
                    {'text': "No"}
                ]
            }},
            {'text': "Grigio", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': {"Hai scelto Grigio"}},
                    {'text': "No"}
                ]
            }},
            {'text': "Nero", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': {"Hai scelto Nero"}},
                    {'text': "No"}
                ]
            }},
        ]
    }
    print("Benvenuto al questionario!\n")
    answers = []
    result = ask_questions(question_tree, answers)
    print(f"\nIl tuo risultato è: {result}")

if __name__ == "__main__":
    main()