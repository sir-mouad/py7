from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        info = {}
        info["name"] = self.name
        info["cost"] = self.cost
        info["rarity"] = self.rarity
        info["type"] = self.__class__.__name__
        if self.__class__.__name__ == "CreatureCard":
            if self.attack < 0 or self.health < 0:
                raise ValueError("the attack or health must be positif")
            info["attack"] = self.attack
            info["health"] = self.health
        return info

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= 5:
            return True
        else:
            return False
