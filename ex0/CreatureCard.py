from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict):
        status = {}
        status = game_state
        status["effect"] = "Creature summoned to battlefield"
        return status

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
