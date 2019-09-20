import helpers


class Card:
    """
    Card object representing a single playing card.
    """

    def __init__(self, suit, value):
        self.suit = suit if suit in helpers.SUITS.keys() else None
        self.value = value if value in helpers.VALUES.keys() else None

    def __str__(self):
        return f"{helpers.VALUES[self.value]} of {helpers.SUITS[self.suit]} [{self.suit}{self.value}]"

    def __repr__(self):
        return str(self)
