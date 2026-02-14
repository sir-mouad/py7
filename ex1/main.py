from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck
print("\n=== DataDeck Deck Builder ===\n")
print("Building deck with different card types...")

cards = Deck()
Creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
Spell = SpellCard("Lightning Bolt", 3, "Common", "damage")
Artifact = ArtifactCard("Healing Potion", 2, "Common",
                        5, "Permanent: +1 mana per turn")
try:
    cards.add_card(Creature)
    cards.add_card(Spell)
    cards.add_card(Artifact)
except ValueError as e:
    print(e)
print("Deck stats:", cards.get_deck_stats())
print("\nDrawing and playing cards:\n")
print("Drew: Lightning Bolt (Spell)")
try:
    print("Play result", Spell.play({"player_mana": 5}))
except ValueError as e:
    print(e)
print("\nDrew: Mana Crystal (Artifact)")
try:
    print("Play result", Artifact.play({"player_mana": 6}))
except ValueError as e:
    print(e)
print("\nDrew: Fire Dragon (Creature)")
try:
    print("Play result", Creature.play({"player_mana": 6}))
except ValueError as e:
    print(e)
print("\nPolymorphism in action: Same interface, different card behaviors")
