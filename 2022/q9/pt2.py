import sys
import numpy as np

dir_codes = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}


def sign(x):
    if x == 0:
        return 0
    return -1 if x < 0 else 1

def update_tail(head, tail):
    delta = head - tail
    if any(np.abs(delta) >= 2):
        if delta[1] == 0 or delta[0] == 0:
            new_tail = head - np.array([sign(x) for x in delta]) # easy
        elif np.abs(delta[0]) == np.abs(delta[1]): # > 2 diagonal step
            new_tail = head - np.array([sign(x) for x in delta])
        else:
            # slightly unclear. Find which delta axis is greater and use that?
            if np.abs(delta[0]) > np.abs(delta[1]):
                new_tail = head - np.array([sign(delta[0]), 0])
            else:
                new_tail = head - np.array([0, sign(delta[1])])
    else:
        new_tail = tail
        
    return new_tail

with open(sys.argv[1], "rt") as fd:
    def pstate(covered, rope):
        symbol = {}
        for c in covered:
            symbol[c] = '*'
        for i,x in enumerate(rope):
            symbol[tuple(x)] = str(i)
        
        min_x = min([x for x,y in symbol.keys()])
        max_x = max([x for x,y in symbol.keys()])
        min_y = min([y for x,y in symbol.keys()])
        max_y = max([y for x,y in symbol.keys()])

#        print(f"range {min_x}-{max_x}, {min_y}-{max_y} {symbol}")
        for y in range(min_y,max_y+1):
            line = [symbol.get((x,y), '.') for x in range(min_x,max_x+1)]
            print("".join(line))

    def parse(line):
        dir, steps = line.strip().split(" ")
        return np.array(dir_codes[dir]), int(steps)

    def update_rope(step, rope):
        new_rope = [rope[0] + step]
        for i in range(1, len(rope)):
            new_rope.append( update_tail(new_rope[-1], rope[i] ) )
        return new_rope

    covered = set()
    rope = [np.array([0,0]) for x in range(10)]

    for line in fd:
        step, count = parse(line)
        print(f"line={line} step={step} count={count}")
        
        for i in range(count):
            rope = update_rope(step, rope)
            #for knot in rope:
            covered.add(tuple(rope[-1]))

            for i in range(1, len(rope)):
                delta = rope[i] - rope[i-1]
                assert all(np.abs(delta) <= 1)

#            print(f"head={head}, tail={tail}, delta={delta}")
        pstate(covered, rope)
#        print("----")

    
print("")

print(len(covered))