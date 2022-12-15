import sys, re
import numpy as np

lines = []
with open(sys.argv[1], "rt") as fd:
    for line in fd:
        lines.append( [(int(x), int(y)) for x,y in re.findall("(\\d+),(\\d+)", line)] )

print(lines)
w = max([x for line in lines for x,y in line])+2
h = max([y for line in lines for x,y in line])+2

print (f"alloc {h} rows x {h} cols")
m = {}

def sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0

NOTHIN=0
WALL=1
SAND=2
to_sym = {WALL: "#", SAND: "o", NOTHIN: "."}

def getat(x,y):
    if y >= h:
        return WALL
    else:
        return m.get((x,y), NOTHIN)

def setat(x,y,v):
    m[(x,y)] = v

for line in lines:
    x,y = line[0]
    for nx, ny in line[1:]:
        dx = sign(nx - x)
        dy = sign(ny - y)
        setat(x,y, WALL)
        while True:
            y += dy
            x += dx
            setat(x,y, WALL)
            if ny == y and nx == x:
                break

def print_state():
    for y in range(0, 12):
        line = "".join([ to_sym[getat(x,y)] for x in range(490,514) ])
        print(line)


# drop sand in
counter = 0
running = True
while running:
    x = 500
    y = 0
    if getat(x,y) != NOTHIN:
        break
    while True:
        if getat(x,y+1) == NOTHIN:
            y += 1
        else:
            if getat(x-1,y+1) == NOTHIN:
                x+=-1
                y+=1
            elif getat(x+1,y+1) == NOTHIN:
                x+=1
                y+=1
            else:
                assert getat(x,y) == NOTHIN
                setat(x,y,SAND)
                assert getat(x,y) == SAND
#                print("hit", {SAND: "sand", WALL: "wall"}[m[y+1,x]], "at", x, y)
                break
    counter += 1
    print_state()
    
print(counter)
