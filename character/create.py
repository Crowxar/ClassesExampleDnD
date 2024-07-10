from . import races
from . import arch

# Define Character class
class Character:
    def __init__(self, name: str, race_instance: races, archetype_instance: arch, level: int = 1):
        self.name = name
        self.race = race_instance
        self.archetype = archetype_instance
        self.level = level 

        # Base attributes
        self.max_hp = 10
        self.max_stam = 10
        

        self.str = 10
        self.int = 10
        self.wis = 10
        self.con = 10
        self.dex = 10
        self.cha = 10

        # Apply race bonus
        self.apply_race_bonus()
        # Apply archetype bonus
        self.apply_archetype_bonus()

        self.health = self.max_hp * self.level
        self.stam = self.max_stam * self.level
        self.max_stam = self.stam
        self.max_hp = self.health

    def apply_race_bonus(self):
        self.str += self.race.str_bonus
        self.int += self.race.int_bonus
        self.wis += self.race.wis_bonus
        self.con += self.race.con_bonus
        self.dex += self.race.dex_bonus
        self.cha += self.race.cha_bonus
        self.max_hp += self.race.hp_bonus
        self.max_stam += self.race.stam_bonus

    def apply_archetype_bonus(self):
        self.str += self.archetype.str_bonus
        self.int += self.archetype.int_bonus
        self.wis += self.archetype.wis_bonus
        self.con += self.archetype.con_bonus
        self.dex += self.archetype.dex_bonus
        self.cha += self.archetype.cha_bonus
        self.max_hp += self.archetype.hp_bonus
        self.max_stam += self.archetype.stam_bonus

    def describe(self):
        print(f"My name is {self.name}, I am a {self.race.name} {self.archetype.name}. I am currently HP={self.health}/{self.max_hp}, Stamina={self.stam}/{self.max_stam}")
        print(f"My attributes are STR={self.str}, INT={self.int}, WIS={self.wis}, CON={self.con}, DEX={self.dex}, CHA={self.cha}\n")


