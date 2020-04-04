import drawlibrary as dl
import naivesim as ns

# todo - refactor functions to accomodate knockoutstage procedure rather than separate functions
# todo - automate this more, rather than in test?
# todo - sort prints by records

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

    def get_knockout_brackets(self):
        return self.knockoutbracket

    def simulate_round(self):
        self.latest_winners = ns.generate_results(self.matchups)
        self.__update_records()
        self.print_results()

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

    def draw_knockout_brackets(self):
        players_by_losses = self.__sort_by_records()
        self.knockoutbracket = dl.draw_knockout_brackets(players_by_losses[0],players_by_losses[1],players_by_losses[2])

    def simulate_ko_round(self):
        bracketsleft = len(self.knockoutbracket)
        # each bracket has 2 matches, except if 1 bracket left
        if bracketsleft is 1:
            # check if semis or final
            pass
        # else bracket is 2 or 4 - refactor below to divide and conquer
        elif bracketsleft is 2:
            pass
        elif bracketsleft is 4:
            for bracket in self.knockoutbracket:
                winners = ns.generate_results(bracket)
            pass
        else:
            print("ERROR")

    def __update_KO_bracket():
        pass

    # assume that winners list and matchups match up
    def print_results(self):
        for i in range(0,len(self.matchups)):
            (p1,p2) = self.matchups[i]
            winner = self.latest_winners[i]
            if winner is p1:
                print(str(p1.get_name()) + " BEATS " + str(p2.get_name()))
            else:
                print(str(p2.get_name()) + " BEATS " + str(p1.get_name()))

    def print_matchups(self):
        for (p1, p2) in self.matchups:
            print(str(p1.get_name()) + " VS " + str(p2.get_name()))

    def print_all_records(self):
        for player in self.active_players:
            name, team, record = player.get_profile()
            (wins, losses) = record
            print(name + " : (" +  str(wins) +"-"+str(losses)+")")
        for player in self.eliminated_players:
            name, team, record = player.get_profile()
            (wins, losses) = record
            print(name + " : (" +  str(wins) +"-"+str(losses)+")")

    def print_active_records(self):
        for player in self.active_players:
            name, team, record = player.get_profile()
            (wins, losses) = record
            print(name + " : (" +  str(wins) +"-"+str(losses)+")")

    # refactor below to print any KO round
    def print_round_of_16(self):
        index = 1
        for bracket in self.knockoutbracket:
            print("Section "+str(index)+":")
            for (p1,p2) in bracket:
                print(str(p1.get_name()) + " VS " + str(p2.get_name()))
            index +=1

    def print_KO_results():
        pass
