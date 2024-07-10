# Define Race class
class Race:
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

# Define specific Race subclass (Human)
class Human(Race):
    def __init__(self):
        super().__init__("Human",
                         str_bonus=1,
                         int_bonus=1,
                         wis_bonus=1,
                         con_bonus=1,
                         dex_bonus=1,
                         cha_bonus=1)