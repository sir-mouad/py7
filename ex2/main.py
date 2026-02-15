from .EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    EliteCard.Elite_Card()
    print("\nPlaying Arcane Warrior (Elite Card):\n")
    print("Combat phase:")
    card = EliteCard("Arcane Warrior", 5, "Uncommon", 5, "melee", 3, 10)
    print("Attack result:", card.attack("Enemy"))
    print("Defense result:", card.defend(5))
    print("Spell cast:", card.cast_spell("Fireball", ['Enemy1', 'Enemy2']))
    print("Mana channel:", card.channel_mana(10))
    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
