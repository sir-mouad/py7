from ex4 import Card, Combatable
from ex4.Rankable import Rankable
from abc import ABCMeta


class TournamentCard(Card, Combatable, Rankable, metaclass=ABCMeta):
    def __init__(self, name: str, cost: int,
                 rarity: str, wins: int, loses: int, rating: int, id: str):
        super().__init__(name, cost, rarity)
        self.update_wins(wins)
        self.update_losses(loses)
        self.rating = rating
        self.id = id
        self.wins = wins
        self.loses = loses

    def play(self, game_state: dict) -> dict:
        return super().play(game_state)

    def attack(self, target) -> dict:
        return super().attack(target)

    def defend(self, incoming_damage):
        return super().defend(incoming_damage)

    def calculate_rating(self) -> int:
        return self.rating

    def get_combat_stats(self):
        return super().get_combat_stats()

    def get_rank_info(self):
        return super().get_rank_info()

    def update_losses(self, loses):
        return super().update_losses(loses)

    def update_wins(self, wins):
        return super().update_wins(wins)

    def get_tournament_stats(self) -> dict:
        return {
            "wins": self.wins,
            "loses": self.loses,
            "rating": self.rating
        }
