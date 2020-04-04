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

# 1 on 5-0, 5 on 4-1, 10 on 3-2
# 16 players so 4 brackets of 4
def draw_knockout_brackets(perfectplayer, onelossplayers, twolossplayers):
    if len(perfectplayer) + len(onelossplayers) + len(twolossplayers) != 16:
        print("ERROR!")
    else:
        bracket1 = []
        bracket2 = []
        bracket3 = []
        bracket4 = []
        drawnp = random.choice(twolossplayers)
        twolossplayers.remove(drawnp)
        seededp = perfectplayer[0]
        bracket1 += [(seededp, drawnp)]
        drawnp1 = random.choice(twolossplayers)
        twolossplayers.remove(drawnp1)
        drawnp2 = random.choice(twolossplayers)
        twolossplayers.remove(drawnp2)
        bracket1 += [(drawnp1, drawnp2)]

        drawnp = random.choice(twolossplayers)
        twolossplayers.remove(drawnp)
        seededp = random.choice(onelossplayers)
        onelossplayers.remove(seededp)
        bracket2 += [(seededp, drawnp)]
        drawnp1 = random.choice(twolossplayers)
        twolossplayers.remove(drawnp1)
        drawnp2 = random.choice(twolossplayers)
        twolossplayers.remove(drawnp2)
        bracket2 += [(drawnp1, drawnp2)]

        drawnp = random.choice(twolossplayers)
        twolossplayers.remove(drawnp)
        seededp = random.choice(onelossplayers)
        onelossplayers.remove(seededp)
        bracket3 += [(seededp, drawnp)]
        drawnp = random.choice(twolossplayers)
        twolossplayers.remove(drawnp)
        seededp = random.choice(onelossplayers)
        onelossplayers.remove(seededp)
        bracket3 += [(seededp, drawnp)]

        drawnp = random.choice(twolossplayers)
        twolossplayers.remove(drawnp)
        seededp = random.choice(onelossplayers)
        onelossplayers.remove(seededp)
        bracket4 += [(seededp, drawnp)]
        drawnp = random.choice(twolossplayers)
        twolossplayers.remove(drawnp)
        seededp = random.choice(onelossplayers)
        onelossplayers.remove(seededp)
        bracket4 += [(seededp, drawnp)]

        return [bracket1, bracket2, bracket3, bracket4]
