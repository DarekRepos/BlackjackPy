import random

from Cards import Card
from Suit import Suit


class Deck:
    def __init__(self) -> None:
        self._cards = [Card(r + 1, s) for r in range(13) for s in iter(Suit)]
        random.shuffle(self._cards)

    def pop(self) -> Card:
        return self._cards.pop()

    def __bool__(self):
        return bool(self._cards)