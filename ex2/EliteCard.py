from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 damage: int, combat_type: str, damage_bloked, health: int):
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.combat_type = combat_type
        self.damage_bloked = damage_bloked
        self.health = health

    def play(self, game_state: dict) -> dict:
        if game_state["player_mana"] >= 5:
            play_res = {'card_played': self.name,
                        'mana_used': 3,
                        'effect': "Creature summoned to battlefield"
                        }
            game_state["player_mana"] = game_state["player_mana"] - 3
            return play_res
        else:
            raise ValueError("is_playable: False")

    def attack(self, target: str) -> dict:
        card_attak = {"attacker": self.name,
                      "target": target,
                      "damage": self.damage,
                      "combat_type": self.combat_type
                      }
        return card_attak

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = incoming_damage - self.damage_bloked
        if self.health - incoming_damage > 0:
            still_alive = True
        else:
            still_alive = False
        card_defend = {"defender": self.name,
                       "Damage taken": damage_taken,
                       "damage_blocked": self.damage_bloked,
                       "still_alive": still_alive
                       }
        return card_defend

    def get_combat_stats(self) -> dict:
        if self.damage >= 10:
            return {"player_card": self.name, "stats": "WIN"}
        else:
            return {"player_card": self.name, "stats": "LOSE"}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        cast = {"caster": self.name,
                "spell": spell_name,
                "targets": targets,
                "mana_used": 4
                }
        return cast

    def channel_mana(self, amount: int) -> dict:
        channel = {"channeled": 3,
                   "total_mana": amount - 3
                   }
        return channel

    def get_magic_stats(self) -> dict:
        return {"player_mana": 3}

    def Elite_Card() -> None:
        card_m = [Card.play.__name__,
                  Card.get_card_info.__name__,
                  Card.is_playable.__name__
                  ]
        combatable_m = [Combatable.attack.__name__,
                        Combatable.defend.__name__,
                        Combatable.get_combat_stats.__name__
                        ]
        magical_m = [Magical.cast_spell.__name__,
                     Magical.channel_mana.__name__,
                     Magical.get_magic_stats.__name__
                     ]
        print("- Card:", card_m)
        print("- Combatable", combatable_m)
        print("- Magical", magical_m)
