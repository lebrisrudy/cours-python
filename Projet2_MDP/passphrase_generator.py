#!/usr/bin/env python
# passphrase_generator.py
import random
import wordlist

class PassphraseGenerator:
    def __init__(self, wordlist):
        self.wordlist = wordlist

    def generate_passphrase(self, num_words):
        if num_words <= 0:
            raise ValueError("Le nombre de mots dans la passphrase doit être supérieur à zéro.")

        passphrase = [random.choice(self.wordlist) for _ in range(num_words)]
        return " ".join(passphrase)



