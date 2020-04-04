#  import names
import playerprofile
import tournamentmaster

NAMES = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","AA","BB","CC","DD","EE","FF"]
TEAM = "Fnatic"

def test_swiss_stage():
    players = []
    for i in range(0,32):
        players += [playerprofile.Player(NAMES[i],TEAM)]
    tn = tournamentmaster.Tournamentmaster(players)
    tn.draw_matchups()
    print("FIRST ROUND:")
    tn.print_matchups()
    print("~~ SIMULATING ROUND ~~")
    tn.simulate_round()
    print("~~ RECORDS AFTER ROUND 1")
    tn.print_all_records()

test_swiss_stage()
