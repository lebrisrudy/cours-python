#!/usr/bin/env python
# main.py
import random
from question import Question

def generate_questions():
    questions = []
    # Ajoutez vos 10 questions ici
    # Par exemple :
    q1 = Question("Quelle est la capitale de la France?",
                  ["a) Paris", "b) Londres", "c) Berlin"],
                  "a")
    q2 = Question("Quel est le symbole chimique de l'oxygène?",
                  ["a) O", "b) Ox", "c) O2"],
                  "a")
    q3 = Question("Qui a peint la Joconde?",
                  ["a) Pablo Picasso", "b) Vincent van Gogh", "c) Léonard de Vinci"],
                  "c")
    q4 = Question("Quel est le plus grand organe du corps humain?",
                  ["a) Le foie", "b) La peau", "c) Le cœur"],
                  "b")
    q5 = Question("Quel est l'élément le plus abondant dans l'atmosphère terrestre?",
                  ["a) Oxygène", "b) Azote", "c) Hydrogène"],
                  "b")
    q6 = Question("Quel est le symbole chimique de l'or?",
                  ["a) Ag", "b) Au", "c) Fe"],
                  "b")
    q7 = Question("Combien de continents y a-t-il sur Terre?",
                  ["a) 5", "b) 6", "c) 7"],
                  "c")
    q8 = Question("Quel est le plus grand océan du monde?",
                  ["a) L'océan Atlantique", "b) L'océan Arctique", "c) L'océan Pacifique"],
                  "c")
    q9 = Question("Qui a écrit 'Roméo et Juliette'?",
                  ["a) Charles Dickens", "b) William Shakespeare", "c) Jane Austen"],
                  "b")
    q10 = Question("Quel est le plus grand désert du monde?",
                   ["a) Le Sahara", "b) L'Antarctique", "c) L'Arctique"],
                   "b")
    # Ajout des questions dans la liste :
    questions.extend([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10])
    return questions

def main():
    questions = generate_questions()
    random.shuffle(questions)
    score = 0

    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question.get_question_text()}")
        options = question.get_options()
        for option in options:
            print(option)
        user_answer = input("Votre réponse (a, b ou c) : ")
        if question.check_answer(user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Faux! La réponse correcte était {question.get_correct_option()}\n")

    print(f"Score final : {score}/{len(questions)}")
    print("Corrigé :")
    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question.get_question_text()}")
        print(f"Réponse correcte : {question.get_correct_option()}\n")

if __name__ == "__main__":
    main()

