from ex0.CreatureCard import CreatureCard
from ex1 import ArtifactCard, Deck, SpellCard

print("\n=== DataDeck Deck Builder ===\n")
print("Building deck with different card types...")
spell = SpellCard("Lightning Bolt", 3,
                  "rare", "Deal 3 damage to target")
artifact = ArtifactCard("Mana crystal", 2, "rare",
                        4, "Permanent: +1 mana per turn")
creature = CreatureCard("Fire Dragon", 5, "Legendary", 3, 5)
deck = Deck()
deck.add_card(spell)
deck.add_card(artifact)
deck.add_card(creature)
print(f"Deck stats: {deck.get_deck_stats()}")
print("\nDrawing and playing cards:\n")
deck.draw_card()
print("Polymorphism in action: Same interface, different card behaviors!")
