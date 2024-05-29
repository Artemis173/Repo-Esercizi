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

    if node['question'] != "Sei sicuro?":
        answers.append(next_node['text'])

    if 'next' in next_node:
        return ask_questions(next_node['next'], answers, node)
    elif 'result' in next_node:
        return next_node['result']
    else:
        if next_node['text'].lower() == "no":
            if answers: answers.pop()
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

def ask_final_questions(final_node, answers):
    if 'question' not in final_node:
        return final_node['result']

    print(final_node['question'])
    for i, option in enumerate(final_node['options'], 1):
        print(f"  {i}. {option['text']}")
    answer = input("Inserisci il numero della tua risposta: ")
    while not answer.isdigit() or int(answer) < 1 or int(answer) > len(final_node['options']):
        answer = input("Risposta non valida. Inserisci il numero della tua risposta: ")

    answer_index = int(answer) - 1
    next_node = final_node['options'][answer_index]

    if 'next' in next_node:
        return ask_final_questions(next_node['next'], answers)
    elif 'result' in next_node:
        return next_node['result']
    else:
        if next_node['text'].lower() == "no":
            return ask_final_questions(final_node, answers)
        else:
            return ask_final_questions(next_node, answers)

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

    # Strutture ad albero per le domande finali
    final_question_trees = {
        "Rosso": {
            'question': "Qual è la tua stagione preferita?",
            'options': [
                {'text': "Primavera", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'next': {
                            'question': "Cosa ti piace di più della primavera?",
                            'options': [
                                {'text': "Fiori", 'result': "Hai scelto Fiori in primavera"},
                                {'text': "Animali", 'result': "Hai scelto Animali in primavera"},
                                {'text': "Tempo", 'result': "Hai scelto Tempo in primavera"},
                                {'text': "Gite", 'result': "Hai scelto Gite in primavera"},
                                {'text': "Altro", 'result': "Hai scelto Altro in primavera"}
                            ]
                        }},
                        {'text': "No"}
                    ]
                }},
                {'text': "Estate", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'next': {
                            'question': "Cosa ti piace di più dell'estate?",
                            'options': [
                                {'text': "Mare", 'result': "Hai scelto Mare in estate"},
                                {'text': "Vacanze", 'result': "Hai scelto Vacanze in estate"},
                                {'text': "Sole", 'result': "Hai scelto Sole in estate"},
                                {'text': "Gite", 'result': "Hai scelto Gite in estate"},
                                {'text': "Altro", 'result': "Hai scelto Altro in estate"}
                            ]
                        }},
                        {'text': "No"}
                    ]
                }},
                {'text': "Autunno", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'next': {
                            'question': "Cosa ti piace di più dell'autunno?",
                            'options': [
                                {'text': "Foglie", 'result': "Hai scelto Foglie in autunno"},
                                {'text': "Clima", 'result': "Hai scelto Clima in autunno"},
                                {'text': "Cibo", 'result': "Hai scelto Cibo in autunno"},
                                {'text': "Gite", 'result': "Hai scelto Gite in autunno"},
                                {'text': "Altro", 'result': "Hai scelto Altro in autunno"}
                            ]
                        }},
                        {'text': "No"}
                    ]
                }},
                {'text': "Inverno", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'next': {
                            'question': "Cosa ti piace di più dell'inverno?",
                            'options': [
                                {'text': "Neve", 'result': "Hai scelto Neve in inverno"},
                                {'text': "Natale", 'result': "Hai scelto Natale in inverno"},
                                {'text': "Freddo", 'result': "Hai scelto Freddo in inverno"},
                                {'text': "Gite", 'result': "Hai scelto Gite in inverno"},
                                {'text': "Altro", 'result': "Hai scelto Altro in inverno"}
                            ]
                        }},
                        {'text': "No"}
                    ]
                }}
            ]
        },
        "Giallo": {
            'question': "Quale attività preferisci?",
            'options': [
                {'text': "Sportiva", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'next': {
                            'question': "Quale sport preferisci?",
                            'options': [
                                {'text': "Calcio", 'result': "Hai scelto Calcio"},
                                {'text': "Basket", 'result': "Hai scelto Basket"},
                                {'text': "Nuoto", 'result': "Hai scelto Nuoto"},
                                {'text': "Ciclismo", 'result': "Hai scelto Ciclismo"},
                                {'text': "Altro", 'result': "Hai scelto Altro"}
                            ]
                        }},
                        {'text': "No"}
                    ]
                }},
                {'text': "Creativa", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'next': {
                            'question': "Quale attività creativa preferisci?",
                            'options': [
                                {'text': "Pittura", 'result': "Hai scelto Pittura"},
                                {'text': "Scrittura", 'result': "Hai scelto Scrittura"},
                                {'text': "Musica", 'result': "Hai scelto Musica"},
                                {'text': "Fotografia", 'result': "Hai scelto Fotografia"},
                                {'text': "Altro", 'result': "Hai scelto Altro"}
                            ]
                        }},
                        {'text': "No"}
                    ]
                }},
                {'text': "Culturale", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'next': {
                            'question': "Quale attività culturale preferisci?",
                            'options': [
                                {'text': "Visite a musei", 'result': "Hai scelto Visite a musei"},
                                {'text': "Lettura di libri", 'result': "Hai scelto Lettura di libri"},
                                {'text': "Frequentare concerti", 'result': "Hai scelto Frequentare concerti"},
                                {'text': "Guardare film", 'result': "Hai scelto Guardare film"},
                                {'text': "Altro", 'result': "Hai scelto Altro"}
                            ]
                        }},
                        {'text': "No"}
                    ]
                }},
                {'text': "Rilassante", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'next': {
                            'question': "Quale attività rilassante preferisci?",
                            'options': [
                                {'text': "Yoga", 'result': "Hai scelto Yoga"},
                                {'text': "Meditazione", 'result': "Hai scelto Meditazione"},
                                {'text': "Escursioni in natura", 'result': "Hai scelto Escursioni in natura"},
                                {'text': "Bagno caldo", 'result': "Hai scelto Bagno caldo"},
                                {'text': "Altro", 'result': "Hai scelto Altro"}
                            ]
                        }},
                        {'text': "No"}
                    ]
                }}
            ]
        },
        "Blu": {
            'question': "Qual è il tuo hobby preferito?",
            'options': [
                {'text': "Lettura", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'result': "Hai scelto Lettura"},
                        {'text': "No"}
                    ]
                }},
                {'text': "Sport", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'result': "Hai scelto Sport"},
                        {'text': "No"}
                    ]
                }},
                {'text': "Musica", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'result': "Hai scelto Musica"},
                        {'text': "No"}
                    ]
                }},
                {'text': "Cucina", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'result': "Hai scelto Cucina"},
                        {'text': "No"}
                    ]
                }},
                {'text': "Arte", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'result': "Hai scelto Arte"},
                        {'text': "No"}
                    ]
                }}
            ]
        },
        "Arancio": {
            'question': "Qual è il tuo cibo preferito?",
            'options': [
                {'text': "Pizza", 'result': "Hai scelto Pizza"},
                {'text': "Pasta", 'result': "Hai scelto Pasta"},
                {'text': "Sushi", 'result': "Hai scelto Sushi"},
                {'text': "Hamburger", 'result': "Hai scelto Hamburger"},
                {'text': "Insalata", 'result': "Hai scelto Insalata"}
            ]
        },
        "Verde": {
            'question': "Qual è il tuo animale preferito?",
            'options': [
                {'text': "Cane", 'result': "Hai scelto Cane"},
                {'text': "Gatto", 'result': "Hai scelto Gatto"},
                {'text': "Uccello", 'result': "Hai scelto Uccello"},
                {'text': "Pesce", 'result': "Hai scelto Pesce"},
                {'text': "Coniglio", 'result': "Hai scelto Coniglio"}
            ]
        },
        "Viola": {
            'question': "Quale è la tua bevanda preferita?",
            'options': [
                {'text': "Caffè", 'result': "Hai scelto Caffè"},
                {'text': "Tè", 'result': "Hai scelto Tè"},
                {'text': "Succhi di frutta", 'result': "Hai scelto Succhi di frutta"},
                {'text': "Birra", 'result': "Hai scelto Birra"},
                {'text': "Vino", 'result': "Hai scelto Vino"}
            ]
        },
        "Bianco": {
            'question': "Qual è il tuo film preferito?",
            'options': [
                {'text': "Drammatico", 'result': "Hai scelto un film Drammatico"},
                {'text': "Commedia", 'result': "Hai scelto un film Commedia"},
                {'text': "Azione", 'result': "Hai scelto un film d'Azione"},
                {'text': "Fantascienza", 'result': "Hai scelto un film di Fantascienza"},
                {'text': "Horror", 'result': "Hai scelto un film Horror"}
            ]
        },
        "Grigio": {
            'question': "Qual è il tuo luogo preferito?",
            'options': [
                {'text': "Mare", 'result': "Hai scelto Mare"},
                {'text': "Montagna", 'result': "Hai scelto Montagna"},
                {'text': "Città", 'result': "Hai scelto Città"},
                {'text': "Campagna", 'result': "Hai scelto Campagna"},
                {'text': "Deserto", 'result': "Hai scelto Deserto"}
            ]
        },
        "Nero": {
            'question': "Qual è il tuo sport preferito?",
            'options': [
                {'text': "Calcio", 'result': "Hai scelto Calcio"},
                {'text': "Basket", 'result': "Hai scelto Basket"},
                {'text': "Tennis", 'result': "Hai scelto Tennis"},
                {'text': "Nuoto", 'result': "Hai scelto Nuoto"},
                {'text': "Atletica", 'result': "Hai scelto Atletica"}
            ]
        }
    }

    # Inizio del questionario
    answers = []
    color_choice = ask_questions(color_class, answers)
    final_result = ask_final_questions(final_question_trees[color_choice], answers)
    print(final_result)
    
if __name__ == "__main__":
    main()