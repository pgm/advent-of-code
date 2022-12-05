import sys
move_encoding = {"A":"Rock", "B":"Paper", "C":"Scissors",
 "X":"Rock", "Y":"Paper", "Z":"Scissors"}

beats = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
points_for_choice = {"Rock": 1, "Paper": 2, "Scissors": 3}

def points_for_outcome(opponent, mine):
    if opponent == mine: 
        return 3
    elif beats[mine] == opponent:
        return 6
    else:
        return 0

with open(sys.argv[1], "rt") as fd:
    accum = 0
    for line in fd:
        line = line.strip().replace(" ", "")
        opponent, mine = [move_encoding[x] for x in line]
        accum += points_for_choice[mine] + points_for_outcome(opponent, mine)
print(accum)
        
