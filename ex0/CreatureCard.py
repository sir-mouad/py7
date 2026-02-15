from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict):
        if game_state["player_mana"] >= 5:
            play_res = {'card_played': self.name,
                        'mana_used': 3,
                        'effect': "Creature summoned to battlefield"
                        }
            game_state["player_mana"] = game_state["player_mana"] - 3
            return play_res
        else:
            raise ValueError("is_playable: False")

    def attack_target(self, target: str) -> dict:
        attack = {}
        attack["attacker"] = self.name
        attack["target"] = target
        attack["damage_dealt"] = self.attack
        if self.health - self.attack < 0:
            attack["combat_resolved"] = True
        else:
            attack["combat_resolved"] = False
        return attack
