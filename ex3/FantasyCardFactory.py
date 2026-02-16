from ex0.Card import Card
from ex0 import CreatureCard
from ex3 import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.cards = []
        self.creatures = ["dragon", "goblin"]
        self.spells = ["fireball"]
        self.artifacts = ["mana_ring"]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        card = CreatureCard(name_or_power, 1, "Legendary", 1, 20)
        self.cards.append(card)
        return (card)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        card = CreatureCard(name_or_power, 1, "Legendary", 1, 20)
        self.cards.append(card)
        return (card)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        card = CreatureCard(name_or_power, 1, "Legendary", 1, 20)
        self.cards.append(card)
        return (card)

    def create_themed_deck(self,
                           name_or_power: str | int | None = None) -> Card:
        card = CreatureCard(name_or_power, 1, "Legendary", 1, 20)
        self.cards.append(card)
        return (card)

    def get_supported_types(self) -> dict:
        return {
            "creatures": self.creatures,
            "spells": self.spells,
            "artifacts": self.artifacts,
            }
