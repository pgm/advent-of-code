import sys

with open(sys.argv[1], "rt") as fd:
    numbers = [int(line.strip()) for line in fd]

indices = list(range(len(numbers)))

shuffled = list(numbers)

def do_move(elements, i, move):
    v = elements[i]
    del elements[i]
    elements.insert((i+move)%len(elements), v)

for orig_index, move in enumerate(numbers):
    new_index = indices.index(orig_index)
    assert new_index >= 0
    assert shuffled[new_index] == move, f"orig_index={orig_index} move={move}, at index {shuffled[new_index]}"
    do_move(shuffled, new_index, move)
    do_move(indices, new_index, move)

#    print(f"after move {move}: {shuffled}, {indices}")

    new_index = indices.index(orig_index)
    assert new_index >= 0
    assert shuffled[new_index] == move, f"after move, orig_index={orig_index} move={move}, at index {shuffled[new_index]}"


zero_index = shuffled.index(0)
print(sum([shuffled[(x+zero_index)%len(shuffled)] for x in [1000, 2000, 3000]]))
