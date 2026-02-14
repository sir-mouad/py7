from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if game_state["player_mana"] >= 5:
            play_res = {'card_played': self.name,
                        'mana_used': 3,
                        'effect': self.resolve_effect(["target"])
                        }
            game_state["player_mana"] = game_state["player_mana"] - 3
            return play_res
        else:
            raise ValueError("is_playable: False")

    def resolve_effect(self, targets: list) -> dict:
        if self.effect_type == "damage":
            return {"effect": f"Deal {self.cost} damage to target"}

        elif self.effect_type == "heal":
            return {"effect": f"Heal target for {self.cost}"}
        return {"effect": "no effect"}
