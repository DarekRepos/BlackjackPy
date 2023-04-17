from Cards import AceCard, Card, FaceCard
from Suit import Suit


class CardFactory:
    def rank(self, rank: int) -> "CardFactory":
        self.class_, self.rank_str = {
            1: (AceCard, "A"),
            11: (FaceCard, "J"),
            12: (FaceCard, "Q"),
            13: (FaceCard, "K"),
        }.get(rank, (Card, str(rank)))
        return self

    def suit(self, suit: Suit) -> Card:
        return self.class_(self.rank_str, suit)
