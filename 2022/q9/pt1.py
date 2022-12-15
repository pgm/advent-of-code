import sys
import numpy as np

dir_codes = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}

covered = set()
head = np.array([0,0])
tail = np.array([0,0])

def sign(x):
    if x == 0:
        return 0
    return -1 if x < 0 else 1

with open(sys.argv[1], "rt") as fd:
    def pstate():
        for y in range(10):
            def letter(x,y):
                l = '*' if (x,y) in covered else ' '
                if (x,y) == tuple(tail):
                    l = 'T'
                if (x,y) == tuple(head):
                    l = 'H'
                return l
                
            line = [letter(x,y-10-1) for x in range(10)]
            print("".join(line))

    def parse(line):
        dir, steps = line.strip().split(" ")
        return np.array(dir_codes[dir]), int(steps)
        
    covered.add(tuple(tail))
    for line in fd:
        step, count = parse(line)
        #print(f"line={line} step={step} count={count}")
        
        for i in range(count):
            head += step
            
            delta = head - tail
            if any(np.abs(delta) >= 2):
                if delta[1] == 0 or delta[0] == 0:
                    delta = np.array([sign(x) for x in delta])
                elif delta[0] * delta[1] == -1: # one diagonal step
                    delta = np.array([0,0])
                else:
                    if np.abs(delta[0]) > np.abs(delta[1]):
                        delta[0] = sign(delta[0])
                    else:
                        delta[1] = sign(delta[1])
            else:
                delta = np.array([0,0])
                
            tail += delta
            covered.add(tuple(tail))
#            print(f"head={head}, tail={tail}, delta={delta}")
#            pstate()
#            print("----")

    
print("")

print(len(covered))