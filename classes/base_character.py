class Character:
    def __init__(self, name, hit_points):
        self.name = name
        self.hit_points = hit_points

    def take_damage(self, damage):
        self.hit_points -= damage
        if self.hit_points <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage and now has {self.hit_points} hit points.")