import random

class Monster():
    def __init__(self):
        self.name = ''
        self.type = 0
        self.ac = 11
        self.hit_point_max = 0
        self.movement = 0
        self.damage_low = 1
        self.damage_high = 0
        self.morale = ''
        self.treasure_type = 'None'
        self.xp = 0
        
        


    def roll_to_hit(self):
        return random.randint(3, 18)

    def roll_for_damage(self):
        return random.randint(1, 4)

    def get_ac(self):
        return 12
    
    def get_movement(self):
        pass

    

    