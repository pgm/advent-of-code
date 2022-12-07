import sys

def find(txt):
    history = []
    for i, char in enumerate(txt):
        history.append((i, []))
            
        for start_i, h in history:
            h.append(char)

        if len(history) == 4:
            if len(set(history[0][1])) == 4:
                return history[0][0] + 4
            del history[0]
        
    

with open(sys.argv[1], "rt") as fd:
    for line in fd:   
        print(find(line.strip()))