
class Combat():
    def __init__(self, player_characters, non_player_characters, player_ply_function, end_game_function):
        self.player_characters = player_characters
        self.non_player_characters = non_player_characters
        self.interactive_mode = False
        self.party_xp = 0
        self.party_success = False
        self.ordered_combatants = []
        self.player_ply_function = player_ply_function
        self.end_game_function = end_game_function
        
    def are_all_characters_dead(self):
        pass

    def is_combat_over(self):
        pass

    def end_combat(self):
        pass

    def ply(self):
        pass

    def print_stats(self):
        pass

    def turn(self):
        pass
    
    def start(self):
        pass