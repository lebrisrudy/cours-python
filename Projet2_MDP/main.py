#!/usr/bin/env python
# main.py
from password_strength import PasswordStrengthTester
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator
from wordlist import wordlist

def main():
    print("Bienvenue dans l'outil de sécurité !")

    while True:
        print("\nOptions :")
        print("1. Testeur de force de mot de passe")
        print("2. Générateur de mot de passe aléatoire")
        print("3. Générateur de passphrase")
        print("4. Quitter")

        choice = input("Choisissez une option (1/2/3/4) : ")

        if choice == "1":
            password = input("Entrez un mot de passe : ")
            strength = PasswordStrengthTester(password)
            strength.calculate_entropy()

        elif choice == "2":
            num_lowercase = int(input("Nombre de minuscules : "))
            num_uppercase = int(input("Nombre de majuscules : "))
            num_digits = int(input("Nombre de chiffres : "))
            num_special_chars = int(input("Nombre de caractères spéciaux : "))

            gen = PasswordGenerator(num_lowercase, num_uppercase, num_digits, num_special_chars)
            password = gen.generate_password()

            strength = PasswordStrengthTester(password)
            strength.calculate_entropy()

        elif choice == "3":
            generator = PassphraseGenerator(wordlist)
            num_words = int(input("Nombre de mots dans la passphrase : "))
            passphrase = generator.generate_passphrase(num_words)
            print(f"Passphrase générée : {passphrase}")

        elif choice == "4":
            print("Merci d'avoir utilisé notre outil de sécurité !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()


