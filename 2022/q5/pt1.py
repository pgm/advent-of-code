import re
from dataclasses import dataclass
from pprint import pprint
import sys

stacks = []

@dataclass
class Command:
    count : int
    src : int
    dst : int
    
def parse(fd):
    stacks = [ [] for i in range(9) ]
    lines = []
    for line in fd:
        line = line.rstrip()
        if len(line) > 1 and line[1] == '1':
            break
        for i in range(len(stacks)):
            if len(line) > (i * 4 + 1):
                c = line[i*4+1]
                if c != ' ':
                    stacks[i].insert(0,c)
    pprint(stacks)

    fd.readline()
    commands = []
    for command in fd:
        m = re.match("move (\\d+) from (\\d+) to (\\d+)", command)
        assert m
        count = int(m.group(1))
        from_i = int(m.group(2))-1
        to_i = int(m.group(3)) - 1
        commands.append(Command(count=count, dst=to_i, src=from_i))
    return stacks, commands
    
with open(sys.argv[1], "rt") as fd:
    stacks, commands = parse(fd)
    
    for command in commands:
        for i in range(command.count):
            x = stacks[command.src].pop()
            stacks[command.dst].append(x) 
        print("after", command, stacks)
    
    print("answer", ''.join([stacks[i][-1] if len(stacks[i]) > 0 else '.' for i in range(len(stacks)) ]))

        