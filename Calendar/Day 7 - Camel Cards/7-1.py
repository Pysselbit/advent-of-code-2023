# Advent of Code 2023
# Day 7-1: Camel Cards

import functools

CARDS = "23456789TJQKA"

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


class Hand:
    def __init__(self, input):
        self.cards = []
        self.bid = int(input[1])

        for card in input[0]:
            self.cards.append(CARDS.index(card))


def get_type(hand):
    cards = sorted(hand)

    if cards[0] == cards[4]:
        return FIVE_OF_A_KIND

    if cards[0] == cards[3] or cards[1] == cards[4]:
        return FOUR_OF_A_KIND

    if cards[0] == cards[2] and cards[3] == cards[4]:
        return FULL_HOUSE

    if cards[0] == cards[1] and cards[2] == cards[4]:
        return FULL_HOUSE

    if cards[0] == cards[2] or cards[1] == cards[3] or cards[2] == cards[4]:
        return THREE_OF_A_KIND

    if cards[0] == cards[1] and cards[2] == cards[3]:
        return TWO_PAIR

    if cards[0] == cards[1] and cards[3] == cards[4]:
        return TWO_PAIR

    if cards[1] == cards[2] and cards[3] == cards[4]:
        return TWO_PAIR

    if cards[0] == cards[1] or cards[1] == cards[2] or cards[2] == cards[3] or cards[3] == cards[4]:
        return ONE_PAIR

    return HIGH_CARD


def compare(a, b):
    type_a = get_type(a.cards)
    type_b = get_type(b.cards)

    if type_a != type_b:
        return type_a - type_b

    for i in range(len(a.cards)):
        if a.cards[i] != b.cards[i]:
            return a.cards[i] - b.cards[i]

    return 0


with open("input.txt") as file:
    hands = []
    for line in file.readlines():
        hands.append(Hand(line.strip().split(" ")))

    hands = sorted(hands, key=functools.cmp_to_key(compare))

    winnings = 0
    for i in range(len(hands)):
        winnings += (i + 1) * hands[i].bid

    print(winnings)
