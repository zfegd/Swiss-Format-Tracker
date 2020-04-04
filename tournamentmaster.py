import drawlibrary as dl
import naivesim as ns

# todo - edit functions to accomodate knockoutstage procedure

class Tournamentmaster:
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
        self.latest_winners = ns.simulate_round(self.matchups)
        self.__update_records()

    def __update_records(self):
        self.games_played += 1
        for i in range(0,len(self.matchups)):
            (p1,p2) = self.matchups[i]
            winner = self.latest_winners[i]
            if winner is p1:
                p1.update_record(True)
                p2.update_record(False)
                (p2w, p2l) = p2.get_record()
                if p2l > 2:
                    self.active_players.remove(p2)
                    self.eliminated_players.append(p2)
            else:
                p2.update_record(True)
                p1.update_record(False)
                (p1w, p1l) = p1.get_record()
                if p1l > 2:
                    self.active_players.remove(p1)
                    self.eliminated_players.append(p1)
        if self.games_played is 5:
            self.knockoutstage = True
            # todo - handle knockoutstage scenario

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

    def print_results(self):
        pass

    def print_matchups(self):
        for (p1, p2) in self.matchups:
            print(str(p1.get_name()) + " VS " + str(p2.get_name()))
