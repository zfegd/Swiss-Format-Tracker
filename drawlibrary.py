import random

# drawing for players of same records only
def draw_matchups(listplayers):
    if len(listplayers) % 2 != 0:
        print("ERROR!")
    else:
        matchups = []
        while len(listplayers) >= 2:
            drawnp1 = random.choice(listplayers)
            listplayers.remove(drawnp1)
            drawnp2 = random.choice(listplayers)
            listplayers.remove(drawnp2)
            matchups += [(drawnp1, drawnp2)]
        return matchups

def draw_knockout_brackets():
    pass
