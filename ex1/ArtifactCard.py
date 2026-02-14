from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if game_state["player_mana"] >= 5:
            play_res = {'card_played': self.name,
                        'mana_used': 2,
                        'effect': self.effect
                        }
            game_state["player_mana"] = game_state["player_mana"] - 2
            return play_res
        else:
            raise ValueError("is_playable: False")

    def activate_ability(self) -> dict:
        return {"effect": "Player gains +1 mana"}
