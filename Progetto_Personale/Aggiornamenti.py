def ask_questions(node, answers, prev_node=None):
    if 'question' not in node:
        return node['result']

    print(node['question'])
    for i, option in enumerate(node['options'], 1):
        print(f"  {i}. {option['text']}")
    answer = input("Inserisci il numero della tua risposta: ")
    while not answer.isdigit() or int(answer) < 1 or int(answer) > len(node['options']):
        answer = input("Risposta non valida. Inserisci il numero della tua risposta: ")

    answer_index = int(answer) - 1
    next_node = node['options'][answer_index]

    # Non aggiungere risposte a "Sei sicuro?"
    if node['question'] != "Sei sicuro?":
        answers.append(next_node['text'])

    if 'next' in next_node:
        return ask_questions(next_node['next'], answers, node)
    elif 'result' in next_node:
        return next_node['result']
    else:
        if next_node['text'].lower() == "no":
            if answers: answers.pop()  # Rimuove l'ultima risposta (il "no")
            return ask_questions(prev_node, answers)
        else:
            return ask_questions(next_node, answers)

def ask_single_question(question_node, answers):
    print(question_node['question'])
    for i, option in enumerate(question_node['options'], 1):
        print(f"  {i}. {option['text']}")
    answer = input("Inserisci il numero della tua risposta: ")
    while not answer.isdigit() or int(answer) < 1 or int(answer) > len(question_node['options']):
        answer = input("Risposta non valida. Inserisci il numero della tua risposta: ")

    answer_index = int(answer) - 1
    choice = question_node['options'][answer_index]['result']
    answers.append(choice)


def calculate_result(answers):
    return "Risultato finale basato sulle risposte."

def main():
    # Struttura ad albero delle domande
    color_class = {
        'question': "Qual è il colore che ti piace di più?",
        'options': [
            {'text': "Rosso", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': "Hai scelto Rosso"},
                    {'text': "No"}
                ]
            }},
            {'text': "Giallo", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': "Hai scelto Giallo"},
                    {'text': "No"}
                ]
            }},
            {'text': "Blu", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': "Hai scelto Blu"},
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
                                    {'text': "Sì", 'result': "Hai scelto Arancio con preferenza Rosso"},
                                    {'text': "No"}
                                ]
                            }},
                            {'text': "Giallo", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': "Hai scelto Arancio con preferenza Giallo"},
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
                                    {'text': "Sì", 'result': "Hai scelto Verde con preferenza Giallo"},
                                    {'text': "No"}
                                ]
                            }},
                            {'text': "Blu", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': "Hai scelto Verde con preferenza Blu"},
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
                                    {'text': "Sì", 'result': "Hai scelto Viola con preferenza Rosso"},
                                    {'text': "No"}
                                ]
                            }},
                            {'text': "Blu", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': "Hai scelto Viola con preferenza Blu"},
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
                    {'text': "Sì", 'result': "Hai scelto Bianco"},
                    {'text': "No"}
                ]
            }},
            {'text': "Grigio", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': "Hai scelto Grigio"},
                    {'text': "No"}
                ]
            }},
            {'text': "Nero", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': "Hai scelto Nero"},
                    {'text': "No"}
                ]
            }},
        ]
    }

    #Domande Generali
    general_questions = [
        {
            'question': "Ti senti più legato al corpo o allo spirito?",
            'options': [
                {'text': "Corpo", 'result': 'corpo'},
                {'text': "Spirito", 'result': 'spirito'}
            ]
        },
        {
            'question': "Preferisci la città o la campagna?",
            'options': [
                {'text': "Città", 'result': 'città'},
                {'text': "Campagna", 'result': 'campagna'}
            ]
        },
        {
            'question': "Ti piace più il mare o la montagna?",
            'options': [
                {'text': "Mare", 'result': 'mare'},
                {'text': "Montagna", 'result': 'montagna'}
            ]
        },
        {
            'question': "Preferisci leggere libri o guardare film?",
            'options': [
                {'text': "Libri", 'result': 'libri'},
                {'text': "Film", 'result': 'film'}
            ]
        }
    ]
    print("Benvenuto al questionario!\n")
    answers = []

    # Continuare con l'albero delle domande
    result = ask_questions(color_class, answers)
    print(f"\nIl tuo risultato è: {result}")
    print(f"\nLe tue risposte sono: {answers}")
    
    # Fare le domande iniziali
    for question in general_questions:
        ask_single_question(question, answers)
    print(answers)

    

if __name__ == "__main__":
    main()