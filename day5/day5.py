import re
from collections import defaultdict

line_re = re.compile(r"([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")

with open("input.txt") as f:
    lines = [
        tuple(map(int, line_re.match(line.strip()).groups())) for line in f.readlines()
    ]


def unit_direction(x1, y1, x2, y2):
    if x1 == x2:
        return complex(0, 1 if y1 < y2 else -1)
    elif y1 == y2:
        return complex(1 if x1 < x2 else -1, 0)
    else:
        return complex(1 if x1 < x2 else -1, 1 if y1 < y2 else -1)


# pt 1
line_diagram = defaultdict(lambda: 0)
for x1, y1, x2, y2 in lines:
    if x1 != x2 and y1 != y2:
        continue
    start = complex(x1, y1)
    end = complex(x2, y2)
    dir = unit_direction(x1, y1, x2, y2)
    while start != end + dir:
        line_diagram[start] += 1
        start += dir

print(len([v for v in line_diagram.values() if v >= 2]))

# pt 2
line_diagram = defaultdict(lambda: 0)
for x1, y1, x2, y2 in lines:
    start = complex(x1, y1)
    end = complex(x2, y2)
    dir = unit_direction(x1, y1, x2, y2)
    while start != end + dir:
        line_diagram[start] += 1
        start += dir

print(len([v for v in line_diagram.values() if v >= 2]))

