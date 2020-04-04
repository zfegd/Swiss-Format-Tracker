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
    for i in range(5):
        tn.draw_matchups()
        print("Current ROUND:")
        tn.print_matchups()
        print("~~ SIMULATING ROUND ~~")
        tn.simulate_round()
        print("~~ RECORDS AFTER ROUND ~~")
        tn.print_all_records()
    print("KNOCKOUT DRAW")
    tn.draw_knockout_brackets()
    tn.print_round_of_16()

test_swiss_stage()
