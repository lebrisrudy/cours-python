#Test unitaire (`test_pass.py`)
from password_strength import PasswordStrengthTester
from password_generator import PasswordGenerator
from passphrase_generator import PassphraseGenerator
import unittest
import random
import string
import math

class TestMDP(unittest.TestCase):

    # Test de force mot de passe faible
    def test_faible_password(self):
        password = "P@ssw0rd"
        print("Test du MDP : ", password)
        strength = PasswordStrengthTester(password)
        strength.calculate_entropy()
        print(' ')

    # Test de force mot de passe fort
    def test_fort_password(self):
        password = "x9DA6heLBxXFFTH#"
        print("Test du MDP : ", password)
        strength = PasswordStrengthTester(password)
        strength.calculate_entropy()
        print(' ')

    # Test génération mot de passe
    def test_gen_password(self):
        num_lowercase = 4
        num_uppercase = 4
        num_digits = 4
        num_special_chars = 2

        print(' ')
        gen = PasswordGenerator(num_lowercase, num_uppercase, num_digits, num_special_chars)
        password = gen.generate_password()

        strength = PasswordStrengthTester(password)
        strength.calculate_entropy()
        print(' ')

    # Test génération passphrase
    def test_gen_passphrase(self):
        generator = PassphraseGenerator()
        passphrase = generator.generate_passphrase()
        print(' ')

if __name__ == '__main__':
    unittest.main()
