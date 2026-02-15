from ex0.CreatureCard import CreatureCard


def main() -> None:
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
    game_status = {"player_mana": 6}
    try:
        res = card.play(game_status)
        print(f"play result: {res}")
    except ValueError as e:
        print(e)
    print("\nFire Dragon attacks Goblin Warrior:")
    res = card.attack_target("Goblin Warrior")
    print("Attack result:", res)
    print("\nTesting insufficient mana (3 available):")
    available_mana = 3
    print(f"playable: {card.is_playable(available_mana)}")
    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
