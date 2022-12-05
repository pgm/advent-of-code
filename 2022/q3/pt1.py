import sys

priorities = { chr(ord('a')+i) : i+1 for i in range(26) }
priorities.update( { chr(ord('A')+i) : i+27 for i in range(26) } )

accum = 0
with open(sys.argv[1], "rt") as fd:
    for line in fd:
        line = line.strip()
        a, b = line[:len(line)//2], line[len(line)//2:]
        shared = set(a).intersection(b)
#        assert len(shared) == 1
        for x in shared:
            accum += priorities[x]
print(accum)        
        