#!/usr/bin/env python
# passphrase_generator.py
import random

class PassphraseGenerator:
    def generate_passphrase(self):

        mot = ''
        niveau = 0
        nnombre = ['1','2','3','4','5','6']
        nmot = ['','','','','','']

        while niveau != 6:
            nombre = ''

            for _ in range(5):
                nombre = nombre + random.choice(nnombre)

            file_path="eff_large_wordlist.txt"

            with open(file_path, 'r') as file:
                for ligne in file:
                    if nombre in ligne:
                        rc = ligne.split()
                        mot = rc[1]
                        nmot[niveau] = mot
                        break
            niveau += 1

        print("Passphrase :")

        for word in nmot:
            print(word, end=" ")
