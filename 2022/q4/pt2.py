import sys

accum = 0
with open(sys.argv[1], "rt") as fd:
    for line in fd:
        line = line.strip()
        a, b = [ [int(x) for x in y.split("-")] for y in line.split(",")]
        
        if not ((a[0] > b[1] or a[1] < b[0])):
            accum += 1
print(accum)

        