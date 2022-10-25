from rpg.character import Character
from rpg.weapon import Weapon
from rpg.armor import Armor
from utils.generator import Generator
from rpg.monster import Monster
from rpg.combat import Combat

print("James Rocks!")

sword = Weapon()
print(sword.name)
sword.load('weapons/sword.json')
print(sword.name)

chainmail = Armor()
chainmail.load('armor/chainmail.json')
print(chainmail.name)

def ply_function(result):
    #print("Hi, I'm the ply function")
    #value = input("Roll the dice.")
    if(result.get("hit")):
        print(f'{result.get("attacker_name")} scored a hit. {result.get("defender_name")} now has {result.get("defender_hp")} hit points left')
    else:
        print(f'{result.get("attacker_name")} missed.')


def end_game_function(winner):
    print(winner)
    print("Game Over")

james = Character()
james.load_from_json('characters/james.json')
print(james.name, james.strength, james.intelligence, james.wisdom, james.dexterity, 
james.charisma, james.constitution, james.class_, james.race, james.level, james.hit_point_max)

monster = Monster()
monster.name = "Skeleton"
monster.hit_point_max = 8
monster.damage_low = 1
monster.damage_high = 4

game = Combat([james], [monster], ply_function, end_game_function)
game.start()



thomas = Character()
thomas.load_from_json('characters/thomas.json')
print(thomas.name, thomas.strength)

generator = Generator()
new_character = generator.character()
print(new_character.hit_point_max, new_character.intelligence, new_character.name, new_character.strength, 
new_character.wisdom, new_character.dexterity, new_character.charisma, new_character.constitution,
new_character.class_, new_character.race)


