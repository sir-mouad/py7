from .CreatureCard import CreatureCard
print("\n=== DataDeck Card Foundation ===\n")
print("esting Abstract Base Class Design:\n")

card = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
try:
    print(card.get_card_info())
except ValueError as e:
    print(e)
print("\nPlaying Fire Dragon with 6 mana available:")
available_mana = 6
print(f"playable: {card.is_playable(available_mana)}")
game_status = {"card_played": card.name, "mana_used": 5}
res = card.play(game_status)
print(f"play result: {game_status}")
print("\nFire Dragon attacks Goblin Warrior:")
res = card.attack_target("Goblin Warrior")
print("Attack result:", res)
print("\nTesting insufficient mana (3 available):")
available_mana = 3
print(f"playable: {card.is_playable(available_mana)}")
print("\nAbstract pattern successfully demonstrated!")
