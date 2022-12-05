x = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

with open("input.txt", "rt") as fd:
    def parse():
        total = 0
        for line in fd:
            line = line.strip()
            if line == "":
                yield total
                total = 0
            else:
                total += int(line)
        yield total

    print(sum(sorted(parse())[-3:]))
