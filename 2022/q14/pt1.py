import sys, re
import numpy as np

lines = []
with open(sys.argv[1], "rt") as fd:
    for line in fd:
        lines.append( [(int(x), int(y)) for x,y in re.findall("(\\d+),(\\d+)", line)] )

print(lines)
w = max([x for line in lines for x,y in line])+10
h = max([y for line in lines for x,y in line])+10

print (f"alloc {h} rows x {h} cols")
m = np.zeros( (h, w), np.int8 )

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

for line in lines:
    x,y = line[0]
    for nx, ny in line[1:]:
        dx = sign(nx - x)
        dy = sign(ny - y)
        m[y,x] = WALL
        while True:
            y += dy
            x += dx
            m[y,x] = WALL
            if ny == y and nx == x:
                break

def print_state():
    for y in range(0, 10):
        line = "".join([ to_sym[m[y,x]] for x in range(494,504) ])
        print(line)

# drop sand in
counter = 0
running = True
while running:
    x = 500
    y = 0
    while True:
        if y+1 >= h:
            print("dropped off")
            running = False
            break

        if m[y+1,x] == NOTHIN:
            y += 1
        else:
            if m[y+1,x-1] == NOTHIN:
                x+=-1
                y+=1

            elif m[y+1, x+1] == NOTHIN:
                x+=1
                y+=1
            else:
                print("before", m[y,x], m[y+1,x])
                assert m[y,x] == NOTHIN
                m[y,x] =SAND
                print("hit", {SAND: "sand", WALL: "wall"}[m[y+1,x]], "at", x, y)
                print(m[y,x], m[y+1,x])
                break
    counter += 1
    print_state()
    
print(counter-1)
