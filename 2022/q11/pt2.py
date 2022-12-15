import re
import sys
from dataclasses import dataclass
from typing import Callable

@dataclass
class Monkey:
    id: int
    items : list
    operation : Callable
    modulo : int
    true_dest : int
    false_dest : int
    inspections : int  = 0

def parse_expr(param1, op, param2):
    e = compile(f"lambda old: {param1} {op} {param2}", 'expr', 'eval')
    return eval(e) 

with open(sys.argv[1], "rt") as fd:
    monkeys = {}
    mdefs = fd.read().split("\n\n")
    for mdef in mdefs:
        m = re.match(
"""Monkey (\\d+):
  Starting items: ([0-9, ]+)
  Operation: new = (\\S+) (.) (\\S+)
  Test: divisible by (\\S+)
    If true: throw to monkey (\\d+)
    If false: throw to monkey (\\d+)""", mdef.strip())
        assert m
        mid, items, param1, op, param2, modulo, true_dest, false_dest = m.groups()
        
        monkeys[int(mid)] = Monkey(int(mid), [int(x.strip()) for x in items.split(",")], parse_expr(param1, op, param2), int(modulo), int(true_dest), int(false_dest))

    print(monkeys)
    accum = 1
    for m in monkeys.values():
        accum *= m.modulo
    mega_modulo = accum
    print("mega_modulo", mega_modulo)
        
    for i in range(10000):
        for mid in sorted(monkeys.keys()):
            m = monkeys[mid]
            while len(m.items) > 0:
                orig_item = item = m.items[0]
                del m.items[0]
                m.inspections += 1
                item = m.operation(item)
                assert item > 0
#                new_value = item//3
                assert (item % mega_modulo) % m.modulo == item % m.modulo
                new_value = item % mega_modulo
                condition = new_value % m.modulo == 0
                if condition:
                    dest = m.true_dest
                else:
                    dest = m.false_dest
#                print(f"monkey {mid}: {orig_item} -> {item} -> {new_value}, {condition}, send to {dest}, {m.inspections}")
                monkeys[dest].items.append(new_value)

        if i +1 in [1, 10, 1000, 2000, 3000, 9000, 10000]:
            for mid in sorted(monkeys.keys()):
                m = monkeys[mid]
                print(f"  round{i+1} Monkey {mid}: inspected: {m.inspections} items:{m.items} ")
    
    most = sorted([m.inspections for m in monkeys.values()])
    print(most[-1] * most[-2])
    