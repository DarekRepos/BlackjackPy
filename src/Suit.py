from enum import Enum

from Cards import AceCard, Card, FaceCard


class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"


cards = [
    AceCard("A", Suit.Spade),
    Card("2", Suit.Spade),
    FaceCard("Q", Suit.Spade),
]


print(cards)
