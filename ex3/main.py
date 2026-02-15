from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    print("\n=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")
    print("Factory: FantasyCardFactory")
    Factory = FantasyCardFactory()
    print("Strategy: AggressiveStrategy")
    Strategy = AggressiveStrategy()
    print(Factory.get_supported_types())
    


if __name__ == "__main__":
    main()
