#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:20:31 2023

@author: dillon
"""

import random

# Read the BIP39 English wordlist from a local file
# word list: https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt
# download as txt file and store in same folder as python script
with open('english.txt', 'r') as f:
    words = f.readlines()

# Select 24 random words from the list
random_words = []
while len(random_words) < 24:
    word = random.choice(words).strip()
    if word not in random_words:
        random_words.append(word)

print(random_words)
