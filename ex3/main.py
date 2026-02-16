from ex3 import AggressiveStrategy, FantasyCardFactory, GameEngine
print("\n=== DataDeck Game Engine ===\n")
engine = GameEngine()
factory = FantasyCardFactory()
factory.create_creature("Fire Dragon (5)")
factory.create_creature("Goblin Warrior (2)")
factory.create_spell("Lightning Bolt (3)")
strategy = AggressiveStrategy()
print("Configuring Fantasy Card Game...")

engine.configure_engine(factory, strategy)
print(f"Available types: {factory.get_supported_types()}")
print("\nSimulating aggressive turn...")
cards = []
for card in engine.factory.cards:
    cards.append(card.name)
print(f"Hand: {cards}")

print("\nTurn execution:")
engine.simulate_turn()
print("\nGame Report:")
print(engine.get_engine_status())
print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
