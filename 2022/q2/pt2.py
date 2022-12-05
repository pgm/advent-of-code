import sys
move_encoding = {"A":"Rock", "B":"Paper", "C":"Scissors",
 "X":"Rock", "Y":"Paper", "Z":"Scissors"}

beats = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
loses = { v : k for k, v in beats.items() }

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

        opponent = move_encoding[line[0]]
        
        if line[1] == "X": # lose
            mine = beats[opponent]
        elif line[1] == "Y": # draw
            mine = opponent
        else: # win
            mine = loses[opponent]
        
#        print(opponent, mine, line[1])
                
        accum += points_for_choice[mine] + points_for_outcome(opponent, mine)
print(accum)
        
