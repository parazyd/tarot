#!/usr/bin/env python3
# See LICENSE file for copyright and license details.
""" Main tarot.py module """

from random import randint
from inspect import cleandoc

from majorarcana import majorarcana, majorarcana_readings, majorarcana_readers


# Configuration
card_deck = majorarcana
readings = majorarcana_readings
readers = majorarcana_readers


cards = [
    "+++ Card 1: How you feel about yourself +++",
    "+++ Card 2: What you want most right now +++",
    "+++ Card 3: Your fears +++",
    "+++ Card 4: What is going for you +++",
    "+++ Card 5: What is going against you +++",
    "+++ Card 6: The likely outcome +++",
]


def draw_random_card(deck):
    return deck[randint(0, len(deck)-1)]


def main():
    reader = readers[randint(0, len(readers)-1)]
    drawn = []

    print("======================================")
    index = 0
    for i in cards:
        print(i)
        card = None
        while True:
            if card in drawn or card is None:
                card = draw_random_card(card_deck)
                continue
            drawn.append(card)
            break
        cardname = list(card.keys())[0]
        print("+++ %s +++" % cardname)
        desc = readings[index][cardname][reader]
        print(cleandoc(desc))
        print("\n======================================")
        index += 1


if __name__ == '__main__':
    main()
