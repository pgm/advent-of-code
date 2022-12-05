import sys

priorities = { chr(ord('a')+i) : i+1 for i in range(26) }
priorities.update( { chr(ord('A')+i) : i+27 for i in range(26) } )

accum = 0
with open(sys.argv[1], "rt") as fd:
    def batch():
        while True:
            line = fd.readline().strip()
            if line == "":
                break
            yield [line, fd.readline().strip(), fd.readline().strip()]

    for b in batch():
        shared = set(b[0]).intersection(b[1]).intersection(b[2])
#        print(shared)
        assert len(shared) ==1
        
        for x in shared:
            accum += priorities[x]
print(accum)        
        