#!/usr/bin/env python
# password_generator.py
import random
import string

class PasswordGenerator:
    def __init__(self, num_lowercase, num_uppercase, num_digits, num_special_chars):
        self.num_uppercase = num_uppercase
        self.num_lowercase = num_lowercase
        self.num_digits = num_digits
        self.num_special_chars = num_special_chars

    def generate_password(self):
        caracteres_majuscules = ''.join(random.choice(string.ascii_uppercase) for _ in range(self.num_uppercase))
        caracteres_minuscules = ''.join(random.choice(string.ascii_lowercase) for _ in range(self.num_lowercase))
        caracteres_chiffres = ''.join(random.choice(string.digits) for _ in range(self.num_digits))
        caracteres_speciaux = ''.join(random.choice(string.punctuation) for _ in range(self.num_special_chars))

        password = ''
        password = caracteres_majuscules + caracteres_minuscules + caracteres_chiffres + caracteres_speciaux
        password = ''.join(random.sample(password, len(password)))

        print(f"Mot de passe généré :", password)

        return password