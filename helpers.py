import random
import card

"""
The possible suits and values of a regular playing card.
"""
SUITS = {"d": "diamonds", "s": "spades", "h": "hearts", "c": "clubs"}
VALUES = {
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "jack",
    12: "queen",
    13: "king",
    14: "ace",
}

"""
The possible actions in blackjack.
Surrender: Fold hand and lose half of bet.
Split: Split a pair (same value) into two hands, double bet and get dealt two new cards, one for each hand.
Double: Double bet and get dealt an extra card.
Hit: get dealt an extra card.
Stand: Hold your hand and end your turn (do nothing and see the game play itself out)
"""
ACTIONS = {"su": "surrender", "sp": "split", "d": "double", "h": "hit", "st": "stand"}


def draw_card():
    """
    Return one random card
    """
    suit = list(SUITS.keys())[random.randint(0, 3)]
    value = random.randint(2, 14)
    return card.Card(suit, value)


def get_correct_action(pair, ace, hand_value, dealer, use_surrender):
    surrender, split, double, hit, stand = ACTIONS.values()
    # Surrender
    if hand_value == 16 and dealer >= 9 and use_surrender:
        return surrender
    if hand_value == 15 and dealer == 10 and use_surrender:
        return surrender

    # Pairs
    if pair:
        card = hand_value / 2
        if ace or card == 8:
            return split
        if card == 9:
            if dealer in list(range(2, 10)) and dealer != 7:
                return split
            return stand
        if card in [2, 3, 7]:
            if dealer in list(range(2, 8)):
                return split
            return hit
        if card == 6:
            if dealer in list(range(2, 7)):
                return split
            return hit
        if card == 5:
            if dealer in list(range(2, 10)):
                return double
            return hit
        if card == 4:
            if dealer in [5, 6]:
                return split
            return hit

    # Ace hand (soft total)
    if ace:
        card = hand_value - 11
        if card == 9:
            return stand
        if card == 8:
            return double if dealer == 6 else stand
        if card == 7:
            if dealer in list(range(2, 7)):
                return double
            if dealer >= 9:
                return hit
            return stand
        if card == 6:
            if dealer in list(range(3, 7)):
                return double
            return hit
        if card in [4, 5]:
            if dealer in [4, 5, 6]:
                return double
            return hit
        if card in [2, 3]:
            if dealer in [5, 6]:
                return double
            return hit

    # Hard total (no ace or ace must be counted as 1)
    if hand_value >= 17:
        return stand
    if hand_value in [13, 14, 15, 16]:
        if dealer in list(range(2, 7)):
            return stand
        return hit
    if hand_value == 12:
        if dealer in [4, 5, 6]:
            return stand
        return hit
    if hand_value == 11:
        return double
    if hand_value == 10:
        if dealer in list(range(2, 10)):
            return double
        return hit
    if hand_value == 9:
        if dealer in [3, 4, 5, 6]:
            return double
        return hit
    if hand_value in [5, 6, 7, 8]:
        return hit


def print_line(n):
    print(f"{'='*n}||{'='*n}")
