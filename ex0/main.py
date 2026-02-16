from ex0.CreatureCard import CreatureCard

print("\n=== DataDeck Card Foundation ===\n")
print("Testing Abstract Base Class Design:\n")
print("CreatureCard Info:")
fire_dragon = CreatureCard(
    name="Fire Dragon",
    cost=5,
    rarity="Legendary",
    attack=7,
    health=5)
print(fire_dragon.get_card_info())
mana = 6
print(f"Playing {fire_dragon.name} with {mana} mana available:")
print(f"Playable: {fire_dragon.is_playable(mana)}")
print(f"Play result: {fire_dragon.play({})}")
print("\nFire Dragon attacks Goblin Warrior:")
goblin_warrior = CreatureCard(
    name="Goblin Warrior",
    cost=5,
    rarity="Legendary",
    attack=7,
    health=5)
print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")
mana = 3
print(f"Testing insufficient mana ({mana} available)")
print(f"Playable: {fire_dragon.is_playable(mana)}")
print("\nAbstract pattern successfully demonstrated!")
