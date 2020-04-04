# todo: future to track stats eg goals scored
# todo: consider overriding __eq__ function

class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.record = (0,0)

    def get_name(self):
        return self.name

    def get_profile(self):
        return self.name, self.team, self.record

    def get_record(self):
        return self.record

    def update_record(self, winbool):
        (currwin, currloss) = self.record
        if winbool:
            self.record = ((currwin+1), currloss)
        else:
            self.record = (currwin,(currloss+1))
        return True

    def rewrite_record(self, numwins, numloss):
        self.record = (numwins, numloss)
        return True

    def get_games_played(self):
        (currwin, currloss) = self.record
        return currwin+currloss
