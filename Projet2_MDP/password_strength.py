#!/usr/bin/env python
# password_strength.py
import math

class PasswordStrengthTester:
    def __init__(self, password):
        # Définir les critères de l'ANSSI
        self.password = password
        self.min_length = 8
        self.min_entropy = 70

    def calculate_entropy(self):
        lowercase= 'abcdefghijklmnopqrstuvwxyz'
        uppercase= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits= '0123456789'
        special_chars= '!@#$%^&*()_+[]{}|;:,.<>?'

        num_lowercase = 0
        num_uppercase = 0
        num_digits = 0
        num_special_chars = 0

        for char in self.password:
            if char in lowercase:
                num_lowercase = 26
            elif char in uppercase:
                num_uppercase = 26
            elif char in digits:
                num_digits = 10
            elif char in special_chars:
                num_special_chars = 24

        total_characters = num_lowercase+num_uppercase+num_digits+num_special_chars
        entropy = round(len(self.password)*math.log2(total_characters))

        if len(self.password) < self.min_length:
            print(f"Taille trop faible (Entropie : {entropy})")
        elif entropy < self.min_entropy:
            print(f"Faible (Entropie : {entropy})")
        else:
            print(f"Fort (Entropie : {entropy})")


