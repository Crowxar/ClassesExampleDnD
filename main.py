from character import races, create, arch

human_war = create.Character("Tom", races.Human(), arch.Warrior(), 4)
human_war.describe()