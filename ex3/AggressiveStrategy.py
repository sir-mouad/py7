from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        return hand

    def get_strategy_name(self) -> str:
        return "Aggressive strategy"

    def prioritze_targets(self, available_targets: list) -> list:
        return available_targets.sort()
