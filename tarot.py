#!/usr/bin/env python3
# See LICENSE file for copyright and license details.
""" Main tarot.py module """

from inspect import cleandoc
from os.path import join
from random import randint
from sys import argv

from majorarcana import majorarcana, majorarcana_readings, majorarcana_readers


# Configuration
card_deck = majorarcana
readings = majorarcana_readings
readers = majorarcana_readers


cards = [
    'Card 1: How you feel about yourself',
    'Card 2: What you want most right now',
    'Card 3: Your fears',
    'Card 4: What is going for you',
    'Card 5: What is going against you',
    'Card 6: The likely outcome',
]


def draw_random_card(deck):
    return deck[randint(0, len(deck)-1)]


def main(out='html'):
    reader = readers[randint(0, len(readers)-1)]
    drawn = []
    index = 0

    if out == 'html':
        print("""<!DOCTYPE html>
              <html lang="en">
              <head>
                <title>Tarot Card Reading</title>

                <style>
                body {
                    background-color: #eee;
                    margin: 2%;
                }
                </style>
              </head>
              <body>""")

    for i in cards:
        if out == 'text':
            print('+++ %s +++' % i)
        else:
            print('<h2 class="cardmeaning">%s</h2>' % i)
        card = None
        while True:
            if card in drawn or card is None:
                card = draw_random_card(card_deck)
                continue
            drawn.append(card)
            break
        cardname = list(card.keys())[0]
        if out == 'text':
            print('+++ %s +++' % cardname)
        else:
            print('<h2 class="cardname">%s</h2>' % cardname)
        image_path = join('images/majorarcana',
                          cardname.lower().replace(' ', '-') + '.jpg')
        if out == 'html':
            print('<img src="%s">' % image_path)
        desc = readings[index][cardname][reader]
        if out == 'text':
            print(cleandoc(desc))
        else:
            print('<p>%s</p>' % cleandoc(desc))
            print('<hr>')
        index += 1

    if out == 'html':
        print("""</body>
              </html>""")


if __name__ == '__main__':
    if len(argv) > 1 and argv[1] == '--text':
        main(out='text')
    else:
        main(out='html')
