from ex0.Card import Card
import random


class Deck:
    def __init__(self):
        self.card = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.card.append(card)
        else:
            raise ValueError(f"{card} is not a card")

    def remove_card(self, card_name: str) -> bool:
        for card in self.card:
            if card.name == card_name:
                self.card.remove(card)
            return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        else:
            return None

    def get_deck_stats(self) -> dict:
        stats = {"total_card": 0,
                 "Creature": 0,
                 "Spell": 0,
                 "Artifact": 0
                 }
        sum_cost = 0
        total = 0
        for card in self.card:
            if card.__class__.__name__ == "CreatureCard":
                stats["Creature"] += 1
            elif card.__class__.__name__ == "SpellCard":
                stats["Spell"] += 1
            elif card.__class__.__name__ == "ArtifactCard":
                stats["Artifact"] += 1
            sum_cost += card.cost
            total += 1
        stats["total_card"] = total
        stats["avg"] = round(sum_cost / total, 1)
        return stats
