from ex4 import TournamentCard, TournamentPlatform
print("\n=== DataDeck Tournament Platform ===\n")
print("Registering Tournament Cards...\n")
platform = TournamentPlatform()
dragon = TournamentCard(
    name="Fire Dragon",
    cost=5,
    rarity=8,
    wins=0,
    loses=0,
    rating=1200,
    id="dragon_001"
)
wizard = TournamentCard(
    name="Ice Wizard",
    cost=5,
    rarity=8,
    wins=0,
    loses=0,
    rating=1150,
    id="wizard_001"
)
print(platform.register_card(dragon))
print(platform.register_card(wizard))
print("Creating tournament match...")
print(f"Match result: {platform.create_match("dragon_001", "wizard_001")}")
print("\nTournament Leaderboard:")
i = 1
cards = platform.get_leaderboard()
for card in cards:
    print(f"{i}: {card.name} - Rating: {card.rating} ({
        card.wins}-{card.loses})")
    i += 1
print("\nPlatform Report:")
print(platform.generate_tournament_report())
print("\n=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
