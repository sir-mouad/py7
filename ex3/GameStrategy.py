from abc import ABC, abstractmethod


class GameStrategy(ABC):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass
    execute_turn = abstractmethod(execute_turn)

    def get_strategy_name(self) -> str:
        pass
    get_strategy_name = abstractmethod(get_strategy_name)

    def prioritze_targets(self, available_targets: list) -> list:
        pass
    prioritze_targets = abstractmethod(prioritze_targets)
