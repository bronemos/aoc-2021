with open("input.txt") as f:
    positions = list(map(int, f.readline().strip().split(",")))

# pt1
min_fuel = float("+inf")
for position in positions:
    if (fuel := sum([abs(x - position) for x in positions])) < min_fuel:
        min_fuel = fuel
print(min_fuel)

# pt2

min_fuel = float("+inf")
for position in range(max(positions) + 1):
    if (
        fuel := sum(
            [abs(x - position) * (abs(x - position) + 1) // 2 for x in positions]
        )
    ) < min_fuel:
        min_fuel = fuel
print(min_fuel)
