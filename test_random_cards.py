# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:34:58 2023

@author: weinana
"""

import random

def generate_random_card(excluded_cards):
    # Define the suits and ranks
    suits = ['♥', '♣', '♦', '♠']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Generate a unique card not in excluded_cards
    while True:
        suit = random.choice(suits)
        rank = random.choice(ranks)
        card = rank + suit
        if card not in excluded_cards:
            return card

# Generate a random number of cards, between 1 and 20
num_cards = random.randint(1, 20)
random_cards = []
excluded_cards = set()

for _ in range(num_cards):
    card = generate_random_card(excluded_cards)
    random_cards.append(card)
    excluded_cards.add(card)

print(random_cards, num_cards)
