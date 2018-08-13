'''
Poker game.
problem54_poker.txt contains 10 cards, 5 of player 1 and other 5 of player 2.
5H is 5 of Hearts, JS is Jack of Spades etc.
How many times did player 1 win?
'''
from bisect import insort
from collections import Counter
from enum import Enum
from itertools import groupby


class Suit(Enum):
    HEARTS = 'H'
    SPADES = 'S'
    CLUBS = 'C'
    DIAMONDS = 'D'


class Value(Enum):
    TWO = ('2', 2)
    THREE = ('3', 3)
    FOUR = ('4', 4)
    FIVE = ('5', 5)
    SIX = ('6', 6)
    SEVEN = ('7', 7)
    EIGHT = ('8', 8)
    NINE = ('9', 9)
    TEN = ('T', 10)
    JACK = ('J', 11)
    QUEEN = ('Q', 12)
    KING = ('K', 13)
    ACE = ('A', 14)

    def __new__(cls, value, weight):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.weight = weight
        return obj


class Combination(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIRS = 3
    SET = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    CARET = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10


class Card:
    def __init__(self, chars):
        self.value = Value(chars[0])
        self.suit = Suit(chars[1])

    def __lt__(self, other):
        return self.value.weight < other.value.weight

    def __le__(self, other):
        return self.value.weight <= other.value.weight

    def __gt__(self, other):
        return self.value.weight > other.value.weight

    def __ge__(self, other):
        return self.value.weight >= other.value.weight


def all_equal(iterable, keyfn=lambda x: x):
    g = groupby(iterable, keyfn)
    return next(g, True) and not next(g, False)


class Hand:
    def __init__(self, cards):
        if len(cards) != 5:
            raise AttributeError('Wrong cards number')
        self.cards = tuple(cards)

    @property
    def combination_weights(self):
        weights = sorted(map(lambda c: c.value.weight, self.cards), reverse=True)

        straight = True
        for i in range(0, len(weights) - 1):
            if weights[i] - weights[i + 1] != 1:
                straight = False
                break

        if all_equal(self.cards, lambda c: c.suit):
            max_weight = max(weights)
            if straight:
                if max_weight == Value.ACE.weight:
                    return Combination.ROYAL_FLUSH.value, max_weight
                else:
                    return Combination.STRAIGHT_FLUSH.value, max_weight
            else:
                return tuple([Combination.FLUSH.value, *weights])
        else:
            if straight:
                return tuple([Combination.STRAIGHT.value, *weights])
            weight_to_quantity = Counter()
            for k, v in groupby(weights):
                weight_to_quantity[k] += len(list(v))
            quantity_to_weight = dict()
            for k, v in weight_to_quantity.items():
                insort(quantity_to_weight.setdefault(v, list()), k)
            if 4 in quantity_to_weight:
                return tuple([Combination.CARET.value, *reversed(quantity_to_weight[4]), *quantity_to_weight[1]])
            if 3 in quantity_to_weight and 2 in quantity_to_weight:
                return tuple([Combination.FULL_HOUSE.value,
                              *reversed(quantity_to_weight[3]),
                              *reversed(quantity_to_weight[2])])
            if 3 in quantity_to_weight:
                return tuple([Combination.SET.value,
                              *reversed(quantity_to_weight[3]),
                              *reversed(quantity_to_weight[1])])
            if 2 in quantity_to_weight:
                pairs = quantity_to_weight[2]
                comb = Combination.TWO_PAIRS.value if len(pairs) == 2 else Combination.PAIR.value
                return tuple([comb,
                              *reversed(pairs),
                              *reversed(quantity_to_weight[1])])
        return tuple([Combination.HIGH_CARD.value, *weights])


def create_hand(cards_list):
    return Hand(list(map(Card, cards_list)))


lines = []
with open('resources/problem54_poker.txt') as f:
    lines = f.readlines()
player_1_won = 0
for line in lines:
    cards = line.split()
    p1 = create_hand(cards[:5])
    p2 = create_hand(cards[5:])
    if p1.combination_weights > p2.combination_weights:
        player_1_won += 1
print(player_1_won)
