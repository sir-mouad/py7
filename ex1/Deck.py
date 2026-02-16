from ex0.Card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
        return None

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def suffle(self) -> None:
        random.shuffle(self.cards)
        return None

    def draw_card(self) -> Card:
        for card in self.cards:
            if card.__class__.__name__ == "CreatureCard":
                t = "Creature"
            elif card.__class__.__name__ == "ArtifactCard":
                t = "Artifact"
            elif card.__class__.__name__ == "SpellCard":
                t = "Spell"
            print(f"Drew: {card.name} ({t})")
            print(f"Play result: {card.play({})}\n")

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        costs = []
        for card in self.cards:
            costs.append(card.cost)
            if card.__class__.__name__ == "CreatureCard":
                creatures += 1
            elif card.__class__.__name__ == "ArtifactCard":
                artifacts += 1
            elif card.__class__.__name__ == "SpellCard":
                spells += 1
        return {
            "total_cards": len(self.cards),
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": sum(costs) / len(costs),
        }
