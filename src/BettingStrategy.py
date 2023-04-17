import abc


class BettingStrategy(metaclass=abc.ABCMeta):
    def bet(self) -> int:
        return 1

    def record_win(self) -> None:
        pass

    def record_loss(self) -> None:
        pass
