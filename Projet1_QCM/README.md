# QCM en Python - Le BRIS Rudy

Ce projet est un QCM en Python. Il permet de créer un QCM avec 10 questions, chacune ayant 3 réponses possibles. Les questions et les réponses sont gérées à l'aide de classes et d'objets, et le code est organisé en plusieurs fichiers.

## Comment utiliser le programme

1. Télécharger les fichiers `main.py` et `question.py`.
2. Exécuter `main.py` pour lancer le QCM.
3. Répondez aux questions en entrant a, b ou c (la casse n'est pas sensible).
4. À la fin du QCM, le score final et le corrigé seront affichés.

## Personnalisation des questions

1. Pour personnaliser les questions, ouvrir `main.py` et ajoutez des nouvelles questions dans la fonction `generate_questions()`. Chaque question est un objet `Question` avec la question elle-même, les options et la réponse correcte.
2. Ensuite ajouter les variables numérotés des questions dans la liste `questions.extend()`.

## Structure des fichiers

- `question.py`: Contient la classe `Question` pour gérer les questions et les réponses.
- `main.py`: Programme principal pour générer le QCM, poser les questions et afficher les résultats.

## Exemple de question

```python
q1 = Question("Quelle est la capitale de la France?", ["a) Paris", "b) Londres", "c) Berlin"], "a")
q2 = Question("Quel est le symbole chimique de l'oxygène?", ["a) O", "b) Ox", "c) O2"], "a")
q3 = Question("Qui a peint la Joconde?", ["a) Pablo Picasso", "b) Vincent van Gogh", "c) Léonard de Vinci"], "c")
questions.extend([q1, q2, q3])
```

## Test unitaire

1. Télécharger le fichier `test_question.py`.
2. Exécuter le fichier `test_question.py`.