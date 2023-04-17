from ast import Tuple
import sys
from typing import Any, cast
from Cards import Card


class Hand:
    def __init__(self, dealer_card: Card, *cards: Card) -> None:
        self.dealer_card = dealer_card
        self.cards = list(cards)

    @staticmethod
    def freeze(other) -> "Hand":
        hand = Hand(other.dealer_card, *other.cards)
        return hand

    @staticmethod
    def split(other, card0, card1) -> Tuple["Hand", "Hand"]:
        hand0 = Hand(other.dealer_card, other.cards[0], card0)
        hand1 = Hand(other.dealer_card, other.cards[1], card1)
        return hand0, hand1

    def card_append(self, card: Card) -> None:
        self.cards.append(card)

    def hard_total(self) -> int:
        return sum(c.hard for c in self.cards)

    def soft_total(self) -> int:
        return sum(c.soft for c in self.cards)

    def __repr__(self) -> str:
        cards_text = ", ".join(map(repr, self.cards))
        return f"{self.__class__.__name__}({self.dealer_card!r}, {cards_text})"

    def __str__(self) -> str:
        return ", ".join(map(str, self.cards))

    def __format__(self, spec: str) -> str:
        if spec == "":
            return str(self)
        return ", ".join(f"{c:{spec}}" for c in self.cards)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, int):
            return self.total() == cast(int, other)
        try:
            return (
                self.cards == cast(Hand, other).cards
                and self.dealer_card == cast(Hand, other).dealer_card
            )
        except AttributeError:
            return NotImplemented

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, int):
            return self.total() < cast(int, other)
        try:
            return self.total() < cast(Hand, other).total()
        except AttributeError:
            return NotImplemented

    def __le__(self, other: Any) -> bool:
        if isinstance(other, int):
            return self.total() <= cast(int, other)
        try:
            return self.total() <= cast(Hand, other).total()
        except AttributeError:
            return NotImplemented

    def total(self) -> int:
        delta_soft = max(c.soft - c.hard for c in self.cards)
        hard = sum(c.hard for c in self.cards)
        if hard + delta_soft <= 21:
            return hard + delta_soft
        return hard


class FrozenHand(Hand):
    def __init__(self, *args, **kw) -> None:
        if len(args) == 1 and isinstance(args[0], Hand):
            # Clone a hand
            other = cast(Hand, args[0])
            self.dealer_card = other.dealer_card
            self.cards = other.cards
        else:
            # Build a fresh Hand from Card instances.
            super().__init__(*args, **kw)

    def __hash__(self) -> int:
        return sum(hash(c) for c in self.cards) % sys.hash_info.modulus


two = Card(2, "♠")
three = Card(3, "♠")
two_c = Card(2, "♣")
ace = Card(1, "♣")
cards = [ace, two, two_c, three]
h2 = Hand(Card(10, "♠"), Card(5, "♠"), *cards)
print(h2)
h2.total()
