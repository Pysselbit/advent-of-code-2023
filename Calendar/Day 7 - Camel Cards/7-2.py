# Advent of Code 2023
# Day 7-2: Camel Cards

import functools

CARDS = "J23456789TQKA"
J = CARDS.index("J")

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


class Hand:
    def __init__(self, bid, cards):
        self.bid = bid
        self.all_hands = []

        js = []
        for card in cards:
            js.append(card == J)

        get_all_hands(js[0], js[1], js[2], js[3], js[4], cards[0], cards[1], cards[2], cards[3], cards[4], self.all_hands)


def get_all_hands(j0, j1, j2, j3, j4, c0, c1, c2, c3, c4, hands):
    if not (j0 or j1 or j2 or j3 or j4):
        hands.append([c0, c1, c2, c3, c4])

    if j0:
        for i in range(len(CARDS)):
            get_all_hands(False, j1, j2, j3, j4, -i, c1, c2, c3, c4, hands)
    elif j1:
        for i in range(len(CARDS)):
            get_all_hands(j0, False, j2, j3, j4, c0, -i, c2, c3, c4, hands)
    elif j2:
        for i in range(len(CARDS)):
            get_all_hands(j0, j1, False, j3, j4, c0, c1, -i, c3, c4, hands)
    elif j3:
        for i in range(len(CARDS)):
            get_all_hands(j0, j1, j2, False, j4, c0, c1, c2, -i, c4, hands)
    elif j4:
        for i in range(len(CARDS)):
            get_all_hands(j0, j1, j2, j3, False, c0, c1, c2, c3, -i, hands)


def get_type(hand):
    cards = hand.copy()
    for i in range(len(cards)):
        cards[i] = abs(cards[i])
    cards = sorted(cards)

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


def compare_all_hands(a, b):
    ai = bi = 0

    while ai < len(a.all_hands) and bi < len(b.all_hands):
        if compare_hands(a.all_hands[ai], b.all_hands[bi]) < 0:
            ai += 1
        else:
            bi += 1

    return (len(a.all_hands) - ai) - (len(b.all_hands) - bi)


def compare_hands(a, b):
    type_a = get_type(a)
    type_b = get_type(b)

    if type_a != type_b:
        return type_a - type_b

    for i in range(len(a)):
        ac = a[i] if a[i] > 0 else J
        bc = b[i] if b[i] > 0 else J
        if ac != bc:
            return ac - bc

    return 0


with open("input.txt") as file:
    hands = []

    for line in file.readlines():
        input = line.strip().split(" ")

        bid = int(input[1])
        cards = []
        for card in input[0]:
            cards.append(CARDS.index(card))

        hands.append(Hand(bid, cards))

    hands = sorted(hands, key=functools.cmp_to_key(compare_all_hands))

    winnings = 0
    for i in range(len(hands)):
        winnings += (i + 1) * hands[i].bid

    print(winnings)