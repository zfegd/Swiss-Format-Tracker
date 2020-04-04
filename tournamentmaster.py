import drawlibrary as dl
import naivesim as ns

# todo - edit functions to accomodate knockoutstage procedure

class tournamentmaster:
    def __init__(self, players):
        # assume number of players is correct, and always 32 -> so max 5 rounds
        self.active_players = players
        self.eliminated_players = []
        self.games_played = 0
        self.matchups = None
        self.latest_winners = None
        self.knockoutstage = False
        self.knockoutbracket = None

    def get_active_players(self):
        return self.active_players

    def get_all_players(self):
        return self.active_players + self.eliminated_players

    def get_eliminated_players(self):
        return self.eliminated_players

    def get_player(self, name):
        for player in self.active_players:
            if player.name == name:
                return player
        for player in self.eliminated_players:
            if player.name == name:
                return player
        return None

    def get_matchups(self):
        return self.matchups

    def simulate_round(self):
        self.winners = ns.simulate_round(self.matchups)
        self.__update_records()

    def __update_records(self):
        self.games_played += 1
        # update player profiles
        # update active player list
        # update if knockoutstage

    def draw_matchups(self):
        players_by_losses = self.__sort_by_records()
        newmatchups = []
        for i in range(0, self.games_played+1):
            newmatchups += dl.draw_matchups(players_by_losses[i])
        self.matchups = newmatchups

    # sort list of players by records for drawing purposes
    def __sort_by_records(self):
        players_by_losses = {}
        for i in range(0,self.games_played+1):
            players_by_losses[i] = []
        for player in self.active_players:
            (pwin, ploss) = player.get_record()
            players_by_losses[ploss] += [player]
        return players_by_losses
