from rpg.character import Character
from rpg.weapon import Weapon
from rpg.armor import Armor
from utils.generator import Generator

print("James Rocks!")

sword = Weapon()
print(sword.name)
sword.load('weapons/sword.json')
print(sword.name)

chainmail = Armor()
chainmail.load('armor/chainmail.json')
print(chainmail.name)

james = Character()
james.load_from_json('characters/james.json')
print(james.name, james.strength, james.intelligence, james.wisdom, james.dexterity,
 james.charisma, james.constitution, james.class_, james.race, james.level, james.hit_point_max, 
 james.movement, james.armors, james.weapons, james.xp, james.current_armor, james.current_weapon)

generator = Generator()
new_character = generator.character()
print(new_character.hit_point_max, new_character.intelligence, new_character.name, new_character.strength, 
new_character.wisdom, new_character.dexterity, new_character.charisma, new_character.constitution,
new_character.class_, new_character.race, new_character.level, new_character.movement, new_character.armors,
new_character.weapons, new_character.xp, new_character.current_armor, new_character.current_weapon)


