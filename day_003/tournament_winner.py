# Platform          : AlgoExpert
# Problem Name      : Tournament Winner
# Difficulty        : Easy
# Category          : Arrays, Hashmap
# Problem URL       : https://www.algoexpert.io/questions/tournament-winner

def tournamentWinner(competitions, results):
    # Write your code here.
    hmap = {}
    for idx in range(len(competitions)):
        home_team = competitions[idx][0]
        away_team = competitions[idx][1]
        won_team = results[idx]
        if won_team == 0:
            hmap[away_team] = hmap.get(away_team, 0) + 3
        else:
            hmap[home_team] = hmap.get(home_team, 0) + 3

    max_team = ""
    max_value = -1
    for key, value in hmap.items():
        if value > max_value:
            max_value, max_team = value, key
    return max_team