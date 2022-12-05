import sys

accum = 0
with open(sys.argv[1], "rt") as fd:
    for line in fd:
        line = line.strip()
        a, b = [ [int(x) for x in y.split("-")] for y in line.split(",")]
        
        if (a[0] <= b[0] and a[1] >= b[1]) or (b[0] <= a[0] and b[1] >= a[1]):
            accum += 1
print(accum)

        