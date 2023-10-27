# Outil de sécurité en Python - Le BRIS Rudy

Ce projet est un Outil de sécurité en Python. Il permet de tester la force d'un mot de passe en calculant sont entropie selon les normes de l'ANSSI, de générer un mot de passe aléatoire en fonction des critères de l'utilisateur. Ainsi que de générer une passphrase selon la méthode des dés de l'EFF.

## Comment utiliser le programme

1. Télécharger les fichiers `main.py`, `password_strength.py`, `password_generator.py`, `passphrase_generator.py` et `eff_large_wordlist.txt`
2. Exécuter `main.py` pour lancer l'Outil de sécurité.
3. Choisir l'option voulu avec 1, 2, 3 ou 4.

## Structure des fichiers

- `main.py`: Programme principal pour l'affichage du menu et l'appel de fonctions.
- `password_strength.py` : Test le mot de passe écrit par l'utilisateur selon les normes de l'ANSSI. Calcul et affiche sa force et son entropie. Détermine si le mot de passe est trop court (inférieur à 8caractères) ou si son entropie est trop faible (inférieur à 70bits).
- `password_generator.py` : Génére un mot de passe aléatoire selon les critères de l'utilisateur : nombres de minuscules, nombres de majuscules, nombres de chiffres, nombres de caractères spéciaux. Affiche également la force et l'entropie du mot de passe généré.
- `passphrase_generator.py` : Génére une série de 6 nombres de 5 chiffres de 1 à 6, et fait correspondre aux mots dans la liste longue des mot de l'EFF. Cela nous donne une passphrase aléatoire de 6 mots se basant sur la méthode des dés de l'EFF.
- `eff_large_wordlist.txt` : Liste longue des mots clés de l'EFF (nécessaire au lancement de `passphrase_generator.py`).

## Exemple d'appel de fonctions

```python
strength = PasswordStrengthTester(password)
strength.calculate_entropy()

gen = PasswordGenerator(num_lowercase, num_uppercase, num_digits, num_special_chars)
password = gen.generate_password()

generator = PassphraseGenerator()
passphrase = generator.generate_passphrase()
```

## Test unitaire

1. Télécharger le fichier `test_pass.py`.
2. Exécuter le fichier `test_pass.py`.