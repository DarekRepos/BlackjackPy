from typing import Tuple


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()

    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(suit={self.suit!r}, rank={self.rank!r})"

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"


class AceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 1, 11


class FaceCard(Card):
    def _points(self) -> Tuple[int, int]:
        return 10, 10
