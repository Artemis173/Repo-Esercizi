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
                    {'text': "Sì", 'result': "Rosso"},
                    {'text': "No"}
                ]
            }},
            {'text': "Giallo", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': "Giallo"},
                    {'text': "No"}
                ]
            }},
            {'text': "Blu", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': "Blu"},
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
                                    {'text': "Sì", 'result': "Arancio-Rosso"},
                                    {'text': "No"}
                                ]
                            }},
                            {'text': "Giallo", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': "Arancio-Giallo"},
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
                                    {'text': "Sì", 'result': "Verde-Giallo"},
                                    {'text': "No"}
                                ]
                            }},
                            {'text': "Blu", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': "Verde-Blu"},
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
                                    {'text': "Sì", 'result': "Viola-Rosso"},
                                    {'text': "No"}
                                ]
                            }},
                            {'text': "Blu", 'next': {
                                'question': "Sei sicuro?",
                                'options': [
                                    {'text': "Sì", 'result': "Viola-Blu"},
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
                    {'text': "Sì", 'result': "Bianco"},
                    {'text': "No"}
                ]
            }},
            {'text': "Grigio", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': "Grigio"},
                    {'text': "No"}
                ]
            }},
            {'text': "Nero", 'next': {
                'question': "Sei sicuro?",
                'options': [
                    {'text': "Sì", 'result': "Nero"},
                    {'text': "No"}
                ]
            }},
        ]
    }

    # Strutture ad albero per le domande finali
    final_question_trees = {
        "Rosso": {
            'question': "Quando sei sotto pressione, qual è la tua reazione tipica?",
            'options': [
                {'text': "A. Reagisco con passione e determinazione. (Fuoco)"},
                {'text': "B. Mantengo la calma e cerco soluzioni razionali. (Acqua)"},
                {'text': "C. Rimango saldo e resisto alle avversità. (Terra)"},
                {'text': "D. Mi adatto rapidamente e cambio strategia. (Aria)"},
                {'text': "E. Cerco di mantenere la chiarezza mentale e la tranquillità. (Cristallo)"}
            ],
            'next': {
                'question': "Cosa preferisci fare nel tempo libero?",
                'options': [
                    {'text': "A. Esplorare nuovi luoghi e avventure. (Fuoco)"},
                    {'text': "B. Rilassarmi e godermi la pace della natura. (Acqua)"},
                    {'text': "C. Coltivare interessi e hobby che mi appassionano. (Terra)"},
                    {'text': "D. Sperimentare nuove attività e avventure. (Aria)"},
                    {'text': "E. Stimolare la mia mente con nuove idee e progetti. (Cristallo)"}
                ],
                'next': {
                    'question': "Qual è il tuo approccio alla risoluzione dei conflitti?",
                    'options': [
                        {'text': "A. Affronto direttamente il problema con fermezza. (Fuoco)"},
                        {'text': "B. Cerco di trovare un terreno comune e mediare. (Acqua)"},
                        {'text': "C. Mantengo la mia posizione con fermezza. (Terra)"},
                        {'text': "D. Cerco di trovare una soluzione flessibile e adattabile. (Aria)"},
                        {'text': "E. Cerco di mantenere la calma e la lucidità per trovare una soluzione equilibrata. (Cristallo)"}
                    ],
                    'next': {
                        'question': "Cosa ti attrae di più in un libro?",
                        'options': [
                            {'text': "A. Avventura e azione mozzafiato. (Fuoco)"},
                            {'text': "B. Profondità emotiva e introspezione. (Acqua)"},
                            {'text': "C. Conoscenza e saggezza pratica. (Terra)"},
                            {'text': "D. Innovazione e idee rivoluzionarie. (Aria)"},
                            {'text': "E. Ispirazione e visione creativa. (Cristallo)"}
                        ],
                        'next': {
                            'question': "Come ti descriveresti in una parola?",
                            'options': [
                                {'text': "A. Appassionato. (Fuoco)"},
                                {'text': "B. Calmo. (Acqua)"},
                                {'text': "C. Stabile. (Terra)"},
                                {'text': "D. Avventuroso. (Aria)"},
                                {'text': "E. Visionario. (Cristallo)"}
                            ],
                            'next': {
                                'question': "Quale ambiente ti mette più a tuo agio?",
                                'options': [
                                    {'text': "A. Un accogliente camino acceso. (Fuoco)"},
                                    {'text': "B. Una spiaggia tranquilla al tramonto. (Acqua)"},
                                    {'text': "C. Una casa con un giardino rigoglioso. (Terra)"},
                                    {'text': "D. Una città vibrante e dinamica. (Aria)"},
                                    {'text': "E. Uno spazio tranquillo e luminoso con arte e cristalli. (Cristallo)"}
                                ],
                                'next': {
                                    'question': "Cosa ti motiva di più nella vita?",
                                    'options': [
                                        {'text': "A. La passione per ciò che faccio. (Fuoco)"},
                                        {'text': "B. Il desiderio di pace e armonia. (Acqua)"},
                                        {'text': "C. La ricerca di sicurezza e stabilità. (Terra)"},
                                        {'text': "D. L'esplorazione e la scoperta di nuovi orizzonti. (Aria)"},
                                        {'text': "E. La ricerca della verità e della bellezza nel mondo. (Cristallo)"}
                                    ],
                                    'next': {
                                        'question': "Come preferisci trascorrere una serata?",
                                        'options': [
                                            {'text': "A. Partecipando a un evento emozionante o una festa. (Fuoco)"},
                                            {'text': "B. Rilassandoti con una cena tranquilla e una buona lettura. (Acqua)"},
                                            {'text': "C. Trascorrendo del tempo con amici o familiari vicini. (Terra)"},
                                            {'text': "D. Esplorando una nuova attività o luogo. (Aria)"},
                                            {'text': "E. Creando qualcosa di nuovo o riflettendo su idee creative. (Cristallo)"}
                                        ],
                                        'next': {
                                            'question': "Cosa ti attrae di più in una relazione?",
                                            'options': [
                                                {'text': "A. Passione e intensità emotiva. (Fuoco)"},
                                                {'text': "B. Empatia e comprensione reciproca. (Acqua)"},
                                                {'text': "C. Stabilità e fiducia reciproca. (Terra)"},
                                                {'text': "D. Avventura e crescita insieme. (Aria)"},
                                                {'text': "E. Condivisione di ideali e visioni comuni. (Cristallo)"}
                                            ],
                                            'next': {
                                                'question': "Qual è la tua visione della felicità?",
                                                'options': [
                                                    {'text': "A. Realizzare i miei sogni e passioni. (Fuoco)"},
                                                    {'text': "B. Vivere in armonia con me stesso e gli altri. (Acqua)"},
                                                    {'text': "C. Avere una vita stabile e soddisfacente. (Terra)"},
                                                    {'text': "D. Esplorare il mondo e le sue infinite possibilità. (Aria)"},
                                                    {'text': "E. Realizzare il mio pieno potenziale e contribuire al benessere degli altri. (Cristallo)"}
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
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
                                {'text': "Calcio", 'result': "Calcio"},
                                {'text': "Basket", 'result': "Basket"},
                                {'text': "Nuoto", 'result': "Nuoto"},
                                {'text': "Ciclismo", 'result': "Ciclismo"},
                                {'text': "Altro", 'result': "Altro"}
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
                                {'text': "Pittura", 'result': "Pittura"},
                                {'text': "Scrittura", 'result': "Scrittura"},
                                {'text': "Musica", 'result': "Musica"},
                                {'text': "Fotografia", 'result': "Fotografia"},
                                {'text': "Altro", 'result': "Altro"}
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
                                {'text': "Visite a musei", 'result': "Visite a musei"},
                                {'text': "Lettura di libri", 'result': "Lettura di libri"},
                                {'text': "Frequentare concerti", 'result': "Frequentare concerti"},
                                {'text': "Guardare film", 'result': "Guardare film"},
                                {'text': "Altro", 'result': "Altro"}
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
                                {'text': "Yoga", 'result': "Yoga"},
                                {'text': "Meditazione", 'result': "Meditazione"},
                                {'text': "Escursioni in natura", 'result': "Escursioni in natura"},
                                {'text': "Bagno caldo", 'result': "Bagno caldo"},
                                {'text': "Altro", 'result': "Altro"}
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
                        {'text': "Sì", 'result': "Lettura"},
                        {'text': "No"}
                    ]
                }},
                {'text': "Sport", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'result': "Sport"},
                        {'text': "No"}
                    ]
                }},
                {'text': "Musica", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'result': "Musica"},
                        {'text': "No"}
                    ]
                }},
                {'text': "Cucina", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'result': "Cucina"},
                        {'text': "No"}
                    ]
                }},
                {'text': "Arte", 'next': {
                    'question': "Sei sicuro?",
                    'options': [
                        {'text': "Sì", 'result': "Arte"},
                        {'text': "No"}
                    ]
                }}
            ]
        },
        "Arancio-Rosso": {
            'question': "Quando sei sotto pressione, qual è la tua reazione tipica?",
            'options': [
                {'text': "A. Reagisco con passione e determinazione. (Fuoco)"},
                {'text': "B. Mantengo la calma e cerco soluzioni razionali. (Acqua)"},
                {'text': "C. Rimango saldo e resisto alle avversità. (Terra)"},
                {'text': "D. Mi adatto rapidamente e cambio strategia. (Aria)"},
                {'text': "E. Cerco di mantenere la chiarezza mentale e la tranquillità. (Cristallo)"}
            ],
            'next': {
                'question': "Cosa preferisci fare nel tempo libero?",
                'options': [
                    {'text': "A. Esplorare nuovi luoghi e avventure. (Fuoco)"},
                    {'text': "B. Rilassarmi e godermi la pace della natura. (Acqua)"},
                    {'text': "C. Coltivare interessi e hobby che mi appassionano. (Terra)"},
                    {'text': "D. Sperimentare nuove attività e avventure. (Aria)"},
                    {'text': "E. Stimolare la mia mente con nuove idee e progetti. (Cristallo)"}
                ],
                'next': {
                    'question': "Qual è il tuo approccio alla risoluzione dei conflitti?",
                    'options': [
                        {'text': "A. Affronto direttamente il problema con fermezza. (Fuoco)"},
                        {'text': "B. Cerco di trovare un terreno comune e mediare. (Acqua)"},
                        {'text': "C. Mantengo la mia posizione con fermezza. (Terra)"},
                        {'text': "D. Cerco di trovare una soluzione flessibile e adattabile. (Aria)"},
                        {'text': "E. Cerco di mantenere la calma e la lucidità per trovare una soluzione equilibrata. (Cristallo)"}
                    ],
                    'next': {
                        'question': "Cosa ti attrae di più in un libro?",
                        'options': [
                            {'text': "A. Avventura e azione mozzafiato. (Fuoco)"},
                            {'text': "B. Profondità emotiva e introspezione. (Acqua)"},
                            {'text': "C. Conoscenza e saggezza pratica. (Terra)"},
                            {'text': "D. Innovazione e idee rivoluzionarie. (Aria)"},
                            {'text': "E. Ispirazione e visione creativa. (Cristallo)"}
                        ],
                        'next': {
                            'question': "Come ti descriveresti in una parola?",
                            'options': [
                                {'text': "A. Appassionato. (Fuoco)"},
                                {'text': "B. Calmo. (Acqua)"},
                                {'text': "C. Stabile. (Terra)"},
                                {'text': "D. Avventuroso. (Aria)"},
                                {'text': "E. Visionario. (Cristallo)"}
                            ],
                            'next': {
                                'question': "Quale ambiente ti mette più a tuo agio?",
                                'options': [
                                    {'text': "A. Un accogliente camino acceso. (Fuoco)"},
                                    {'text': "B. Una spiaggia tranquilla al tramonto. (Acqua)"},
                                    {'text': "C. Una casa con un giardino rigoglioso. (Terra)"},
                                    {'text': "D. Una città vibrante e dinamica. (Aria)"},
                                    {'text': "E. Uno spazio tranquillo e luminoso con arte e cristalli. (Cristallo)"}
                                ],
                                'next': {
                                    'question': "Cosa ti motiva di più nella vita?",
                                    'options': [
                                        {'text': "A. La passione per ciò che faccio. (Fuoco)"},
                                        {'text': "B. Il desiderio di pace e armonia. (Acqua)"},
                                        {'text': "C. La ricerca di sicurezza e stabilità. (Terra)"},
                                        {'text': "D. L'esplorazione e la scoperta di nuovi orizzonti. (Aria)"},
                                        {'text': "E. La ricerca della verità e della bellezza nel mondo. (Cristallo)"}
                                    ],
                                    'next': {
                                        'question': "Come preferisci trascorrere una serata?",
                                        'options': [
                                            {'text': "A. Partecipando a un evento emozionante o una festa. (Fuoco)"},
                                            {'text': "B. Rilassandoti con una cena tranquilla e una buona lettura. (Acqua)"},
                                            {'text': "C. Trascorrendo del tempo con amici o familiari vicini. (Terra)"},
                                            {'text': "D. Esplorando una nuova attività o luogo. (Aria)"},
                                            {'text': "E. Creando qualcosa di nuovo o riflettendo su idee creative. (Cristallo)"}
                                        ],
                                        'next': {
                                            'question': "Cosa ti attrae di più in una relazione?",
                                            'options': [
                                                {'text': "A. Passione e intensità emotiva. (Fuoco)"},
                                                {'text': "B. Empatia e comprensione reciproca. (Acqua)"},
                                                {'text': "C. Stabilità e fiducia reciproca. (Terra)"},
                                                {'text': "D. Avventura e crescita insieme. (Aria)"},
                                                {'text': "E. Condivisione di ideali e visioni comuni. (Cristallo)"}
                                            ],
                                            'next': {
                                                'question': "Qual è la tua visione della felicità?",
                                                'options': [
                                                    {'text': "A. Realizzare i miei sogni e passioni. (Fuoco)"},
                                                    {'text': "B. Vivere in armonia con me stesso e gli altri. (Acqua)"},
                                                    {'text': "C. Avere una vita stabile e soddisfacente. (Terra)"},
                                                    {'text': "D. Esplorare il mondo e le sue infinite possibilità. (Aria)"},
                                                    {'text': "E. Realizzare il mio pieno potenziale e contribuire al benessere degli altri. (Cristallo)"}
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "Arancio": {
            'question': "Qual è il tuo cibo preferito?",
            'options': [
                {'text': "Pizza", 'result': "Pizza"},
                {'text': "Pasta", 'result': "Pasta"},
                {'text': "Sushi", 'result': "Sushi"},
                {'text': "Hamburger", 'result': "Hamburger"},
                {'text': "Insalata", 'result': "Insalata"}
            ]
        },
        "Verde": {
            'question': "Qual è il tuo animale preferito?",
            'options': [
                {'text': "Cane", 'result': "Cane"},
                {'text': "Gatto", 'result': "Gatto"},
                {'text': "Uccello", 'result': "Uccello"},
                {'text': "Pesce", 'result': "Pesce"},
                {'text': "Coniglio", 'result': "Coniglio"}
            ]
        },
        "Viola-Rosso": {
            'question': "Quando sei sotto pressione, qual è la tua reazione tipica?",
            'options': [
                {'text': "A. Reagisco con passione e determinazione. (Fuoco)"},
                {'text': "B. Mantengo la calma e cerco soluzioni razionali. (Acqua)"},
                {'text': "C. Rimango saldo e resisto alle avversità. (Terra)"},
                {'text': "D. Mi adatto rapidamente e cambio strategia. (Aria)"},
                {'text': "E. Cerco di mantenere la chiarezza mentale e la tranquillità. (Cristallo)"}
            ],
            'next': {
                'question': "Cosa preferisci fare nel tempo libero?",
                'options': [
                    {'text': "A. Esplorare nuovi luoghi e avventure. (Fuoco)"},
                    {'text': "B. Rilassarmi e godermi la pace della natura. (Acqua)"},
                    {'text': "C. Coltivare interessi e hobby che mi appassionano. (Terra)"},
                    {'text': "D. Sperimentare nuove attività e avventure. (Aria)"},
                    {'text': "E. Stimolare la mia mente con nuove idee e progetti. (Cristallo)"}
                ],
                'next': {
                    'question': "Qual è il tuo approccio alla risoluzione dei conflitti?",
                    'options': [
                        {'text': "A. Affronto direttamente il problema con fermezza. (Fuoco)"},
                        {'text': "B. Cerco di trovare un terreno comune e mediare. (Acqua)"},
                        {'text': "C. Mantengo la mia posizione con fermezza. (Terra)"},
                        {'text': "D. Cerco di trovare una soluzione flessibile e adattabile. (Aria)"},
                        {'text': "E. Cerco di mantenere la calma e la lucidità per trovare una soluzione equilibrata. (Cristallo)"}
                    ],
                    'next': {
                        'question': "Cosa ti attrae di più in un libro?",
                        'options': [
                            {'text': "A. Avventura e azione mozzafiato. (Fuoco)"},
                            {'text': "B. Profondità emotiva e introspezione. (Acqua)"},
                            {'text': "C. Conoscenza e saggezza pratica. (Terra)"},
                            {'text': "D. Innovazione e idee rivoluzionarie. (Aria)"},
                            {'text': "E. Ispirazione e visione creativa. (Cristallo)"}
                        ],
                        'next': {
                            'question': "Come ti descriveresti in una parola?",
                            'options': [
                                {'text': "A. Appassionato. (Fuoco)"},
                                {'text': "B. Calmo. (Acqua)"},
                                {'text': "C. Stabile. (Terra)"},
                                {'text': "D. Avventuroso. (Aria)"},
                                {'text': "E. Visionario. (Cristallo)"}
                            ],
                            'next': {
                                'question': "Quale ambiente ti mette più a tuo agio?",
                                'options': [
                                    {'text': "A. Un accogliente camino acceso. (Fuoco)"},
                                    {'text': "B. Una spiaggia tranquilla al tramonto. (Acqua)"},
                                    {'text': "C. Una casa con un giardino rigoglioso. (Terra)"},
                                    {'text': "D. Una città vibrante e dinamica. (Aria)"},
                                    {'text': "E. Uno spazio tranquillo e luminoso con arte e cristalli. (Cristallo)"}
                                ],
                                'next': {
                                    'question': "Cosa ti motiva di più nella vita?",
                                    'options': [
                                        {'text': "A. La passione per ciò che faccio. (Fuoco)"},
                                        {'text': "B. Il desiderio di pace e armonia. (Acqua)"},
                                        {'text': "C. La ricerca di sicurezza e stabilità. (Terra)"},
                                        {'text': "D. L'esplorazione e la scoperta di nuovi orizzonti. (Aria)"},
                                        {'text': "E. La ricerca della verità e della bellezza nel mondo. (Cristallo)"}
                                    ],
                                    'next': {
                                        'question': "Come preferisci trascorrere una serata?",
                                        'options': [
                                            {'text': "A. Partecipando a un evento emozionante o una festa. (Fuoco)"},
                                            {'text': "B. Rilassandoti con una cena tranquilla e una buona lettura. (Acqua)"},
                                            {'text': "C. Trascorrendo del tempo con amici o familiari vicini. (Terra)"},
                                            {'text': "D. Esplorando una nuova attività o luogo. (Aria)"},
                                            {'text': "E. Creando qualcosa di nuovo o riflettendo su idee creative. (Cristallo)"}
                                        ],
                                        'next': {
                                            'question': "Cosa ti attrae di più in una relazione?",
                                            'options': [
                                                {'text': "A. Passione e intensità emotiva. (Fuoco)"},
                                                {'text': "B. Empatia e comprensione reciproca. (Acqua)"},
                                                {'text': "C. Stabilità e fiducia reciproca. (Terra)"},
                                                {'text': "D. Avventura e crescita insieme. (Aria)"},
                                                {'text': "E. Condivisione di ideali e visioni comuni. (Cristallo)"}
                                            ],
                                            'next': {
                                                'question': "Qual è la tua visione della felicità?",
                                                'options': [
                                                    {'text': "A. Realizzare i miei sogni e passioni. (Fuoco)"},
                                                    {'text': "B. Vivere in armonia con me stesso e gli altri. (Acqua)"},
                                                    {'text': "C. Avere una vita stabile e soddisfacente. (Terra)"},
                                                    {'text': "D. Esplorare il mondo e le sue infinite possibilità. (Aria)"},
                                                    {'text': "E. Realizzare il mio pieno potenziale e contribuire al benessere degli altri. (Cristallo)"}
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "Viola": {
            'question': "Quale è la tua bevanda preferita?",
            'options': [
                {'text': "Caffè", 'result': "Caffè"},
                {'text': "Tè", 'result': "Tè"},
                {'text': "Succhi di frutta", 'result': "Succhi di frutta"},
                {'text': "Birra", 'result': "Birra"},
                {'text': "Vino", 'result': "Vino"}
            ]
        },
        "Bianco": {
            'question': "Qual è il tuo film preferito?",
            'options': [
                {'text': "Drammatico", 'result': "un film Drammatico"},
                {'text': "Commedia", 'result': "un film Commedia"},
                {'text': "Azione", 'result': "un film d'Azione"},
                {'text': "Fantascienza", 'result': "un film di Fantascienza"},
                {'text': "Horror", 'result': "un film Horror"}
            ]
        },
        "Grigio": {
            'question': "Qual è il tuo luogo preferito?",
            'options': [
                {'text': "Mare", 'result': "Mare"},
                {'text': "Montagna", 'result': "Montagna"},
                {'text': "Città", 'result': "Città"},
                {'text': "Campagna", 'result': "Campagna"},
                {'text': "Deserto", 'result': "Deserto"}
            ]
        },
        "Nero": {
            'question': "Qual è il tuo sport preferito?",
            'options': [
                {'text': "Calcio", 'result': "Calcio"},
                {'text': "Basket", 'result': "Basket"},
                {'text': "Tennis", 'result': "Tennis"},
                {'text': "Nuoto", 'result': "Nuoto"},
                {'text': "Atletica", 'result': "Atletica"}
            ]
        }
    }

    # Inizio del questionario
    answers = []
    color_choice = ask_questions(color_class, answers)
    print(color_choice)
    final_result = ask_final_questions(final_question_trees[color_choice], answers)
    print(final_result)

if __name__ == "__main__":
    main()