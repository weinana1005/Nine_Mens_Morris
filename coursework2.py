"""
MATH20621 - Coursework 2
Student name: Wei Chung-Yu
Student id:   10680317
Student mail: chung-yu.wei@student.manchester.ac.uk

Do not change any part of this string except to replace
the <tags> with your name, id and university email address.
"""

from random import random

# Problem 1
def new_deck():
    suits = ['♥', '♣', '♦', '♠']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = []

    for suit in suits[:2]:
        for rank in ranks:
            deck.append(rank + suit)

    for suit in suits[2:]:
        for rank in reversed(ranks):
            deck.append(rank + suit)

    return deck


# Problem 2
def riffle(d):
    mid = len(d) // 2
    listA, listB = d[:mid], d[mid:]

    shuffled_deck = []

    while listA or listB:
        prob_listA = len(listA) / (len(listA) + len(listB)) if listA else 0

        if random() < prob_listA or not listB:
            shuffled_deck.append(listA.pop(0))
        else:
            shuffled_deck.append(listB.pop(0))

    return shuffled_deck


# Problem 3
def deal(d, n):
   hands = [[] for _ in range(n)]
   for i, card in enumerate(d):
       player = i % n
       hands[player].append(card)

   min_cards = min(len(hand) for hand in hands)
   for hand in hands:
       if len(hand) > min_cards:
           hand.pop()

   return hands


# Problem 4
def card_value(card):
    suit_value = {'♥': 0, '♣': 1, '♦': 2, '♠': 3}
    rank_value = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    rank = card[:-1]
    suit = card[-1]
    total_value = suit_value[suit] * 100 + rank_value[rank]
    return total_value

def hand_string(h):
    sorted_hand = sorted(h, key=card_value)

    return ' '.join(sorted_hand)
# main() function for all the testing
def main():
    print(new_deck())
    print(riffle(['Q♣', '6♣', '10♠', '9♠', 'J♦', '9♣', '7♣', '8♦', '6♠', '10♣', 'A♦', 'Q♠', 'A♠', '5♦']))
    print(deal(['9♣', '3♦', 'J♦', 'J♥', 'Q♣', '10♠', '5♥', '4♥', 'A♣', 'J♠', '6♣', '6♠', '4♠', '7♠', '2♦', 'K♥', 'J♣', 'A♠', '7♣'], 6))
    print(hand_string(['5♥', '9♦', '10♠', '9♥', '4♠', '8♥', 'Q♥', 'Q♠', 'K♣', '9♠', '2♥', '10♦', 'K♦', '8♦']))
main()
