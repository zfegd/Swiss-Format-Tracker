# randomly simulate matches between players, perhaps add skill rating into player profile
import random

def generate_results(list_matchups):
    winners = []
    for (p1,p2) in list_matchups:
        winners += [random.choice([p1,p2])]
    return winners
