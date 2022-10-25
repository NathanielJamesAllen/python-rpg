from rpg.character import Character
import random

class Generator():
    def __init__(self):
        pass

    def character(self):
        char = Character()
        char.hit_point_max = 6
        char.level = 1
        char.name = "James"
        char.xp = 0
        char.intelligence = random.randint(3, 19)
        char.strength = random.randint(3, 19)
        char.wisdom = random.randint(3, 19)
        char.constitution = random.randint(3, 19)
        char.dexterity = random.randint(3, 19)
        char.charisma = random.randint(3, 19)
        
        char.race = random.choice(["Human", "Dwarf", "Elf"])
        char.class_ = random.choice(["Wizard", "Fighter", "Cleric", "Rogue"])
        
        

        return char