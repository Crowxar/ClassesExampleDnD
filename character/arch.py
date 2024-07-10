
# Define Archetype class
class Archetype:
    def __init__(self, name: str,
                 str_bonus: int = 0,
                 int_bonus: int = 0,
                 wis_bonus: int = 0,
                 con_bonus: int = 0,
                 dex_bonus: int = 0,
                 cha_bonus: int = 0,
                 hp_bonus: int = 0,
                 stam_bonus: int = 0):
        
        self.name = name
        self.str_bonus = str_bonus
        self.int_bonus = int_bonus
        self.wis_bonus = wis_bonus
        self.con_bonus = con_bonus
        self.dex_bonus = dex_bonus
        self.cha_bonus = cha_bonus
        
        self.hp_bonus = hp_bonus
        self.stam_bonus = stam_bonus

# Define specific Archetype subclass (Warrior)
class Warrior(Archetype):
    def __init__(self):
        super().__init__("Warrior",
                         str_bonus=2,
                         con_bonus=2,
                         dex_bonus=2,
                         stam_bonus=3,
                         hp_bonus=3)